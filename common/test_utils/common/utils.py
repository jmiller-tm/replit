# standard libs
import logging
import os
import re
import time
from typing import Any, Callable, Dict, List
from unittest.mock import Mock

log = logging.getLogger(__name__)
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(asctime)s.%(msecs)03d - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def replace_supervisee_version_ids_in_supervisor(
    supervisor_contract_code: str, supervisee_alias_to_version_id: Dict[str, str]
) -> str:
    """
    Due to the fact that supervisor contract currently has to hard code
    its supervisee product version ids, there is a need to search and
    replace them with the actual version ids uploaded into the environment
    both when deploying via CLU or during e2e tests;
    This helper provides that utility and is currently being used both in
    e2e and simulation tests
    Note that the regex takes into account CLU resource dependency syntax
    &{dependent_resource}, working examples can be found under:
    https://regex101.com/r/hx4MRL/1
    """
    if supervisee_alias_to_version_id is None:
        raise ValueError(
            "Must provide supervisee_alias_to_version_id for supervisor contract"
        )

    regex = r"(?P<alias_prefix>alias=[\'\"]?)(?P<alias>[\w\d]*)(?P<pvid_prefix>[\'\"]?,\s*smart_contract_version_id=[\'\"]?)(?P<pvid>[\w\d&{}]*)(?P<suffix>[\'\"]?)"  # noqa: E501

    def replace_ids(match: re.Match):
        supervisee_alias = match.group("alias")
        product_ver_id = supervisee_alias_to_version_id.get(supervisee_alias)
        if product_ver_id is None:
            raise NameError(
                f"Missing {supervisee_alias} in {supervisee_alias_to_version_id}"
            )
        # Defend against constant with no quotes
        separator = "'" if not match.group("suffix") else ""
        return (
            match.group("alias_prefix")
            + match.group("alias")
            + match.group("pvid_prefix")
            + separator
            + product_ver_id
            + match.group("suffix")
            + separator
        )

    return re.sub(pattern=regex, repl=replace_ids, string=supervisor_contract_code)


def replace_schedule_tag_ids_in_contract(
    contractdata: str,
    id_mapping: Dict[str, str],
) -> str:
    """
    Replaces the original scheduler tag ids inside a smart contract with the run-specific ids
    :param contractdata: the smart contract code
    :return: the updated smart contract code
    """
    return _replace_resource_ids_in_contract(
        contractdata=contractdata,
        resource_type="schedule_tag_id",
        id_regex=r"(?P<prefix>scheduler_tag_ids=\[)(?P<ids>.*)(?P<suffix>\])",
        id_mapping=id_mapping,
    )


def replace_workflow_ids_in_contract(
    contractdata: str,
    id_mapping: Dict[str, str],
) -> str:
    """
    Replaces the original workflow definition ids inside a smart contract with the run-specific
    ids, so that contracts uploaded by the e2e framework will use the updated workflow versions

    Note: this will only replace instances of workflows being instantiated using kwargs, i.e.
    either "workflow='{wf_name}'" or "workflow="{wf_name}""
    :param contractdata: str, the smart contract code
    :return: str, the updated smart contract code
    """
    return _replace_resource_ids_in_contract(
        contractdata=contractdata,
        resource_type="workflow_definition_id",
        id_regex=r"(?P<prefix>workflow=)(?P<ids>.*)(?P<suffix>,)",
        id_mapping=id_mapping,
    )


def replace_calendar_ids_in_contract(
    contractdata: str,
    id_mapping: Dict[str, str],
) -> str:
    """
    Replaces the original calendar ids inside a smart contract with the run-specific ids.
    The calendar id can be found in the code in two scenarios:
    as calendar=["&{calendar_id}"] in the case of a hook '@requires' decorator or
    as calendar_ids=["&{calendar_id}"] in the case of a call to vault.get_calendar_events.
    Since calendar ids in smart contracts are CLU resource dependency placeholders the
    default value cannot be used.
    https://regex101.com/r/8Yllhq/1
    :param contractdata: the smart contract code
    :return: the updated smart contract code
    """

    return _replace_resource_ids_in_contract(
        contractdata=contractdata,
        resource_type="calendar",
        id_regex=r"(?P<prefix>calendar(_ids)?=\[)(?P<ids>([\'\"]+[\w\d&{}]*[\'\"]+(,)?( ?))+)(?P<suffix>\])",  # noqa: E501,
        id_mapping=id_mapping,
        match_validation=_validate_clu_resource_syntax,
    )


def _replace_resource_ids_in_contract(
    contractdata: str,
    resource_type: str,
    id_regex: str,
    id_mapping: Dict[str, str],
    match_validation: Callable = None,
) -> str:
    """
    Generic method to replace resource ids in contracts (e.g. workflow definitions, scheduler tags)
    with the ids defined in the id_mapping parameter. This method also handles CLU resource
    dependency placeholders (e.g. calendar_ids in the form '&{CALENDAR_ID}') and gracefully handles
    cases where the CLU mapping is missing, i.e '&{CALENDAR_ID}' is replaced with the mapping found
    in the param id_mapping or replaced by 'CALENDAR_ID.
    :param contractdata: the contract to replace the resource ids in
    :param resource_type: the type of resources to replace. Only used for logging purposes
    :param id_regex: the regular expression to identify resource ids to replace. The regex makes use
    of following named groups:
        - 'prefix' - Optional - anything preceding the identifiers that is needed to identify them
        - 'ids' - the identifiers themselves. These can be comma separated and surrounded by single
        quotes or double quotes (these are replaced by single quotes). Whitespace between
        identifiers is also supported
        - 'suffix' - Optional - anything following the identifiers that is needed to identify them
    The regex match is then replaced by combining the prefix, the mapped identifiers found inside
    the main group, and the suffix
    For example, a contract containing scheduler_tags_ids=['id_1', "id_2"] would use regex
    '(?P<prefix>scheduler_tag_ids=\\[)(?P<ids>.*)(?P<suffix>\\])'.
    'scheduler_tag_ids=[' is identified as the prefix
    'id_1', "id_2"' is identified as the ids and mapped to the e2e ids.
    ']' is identified as the suffix
    the output is scheduler_tag_ids=['id_1, 'id_2']
    :param id_mapping: ids will be replaced based on this mapping, else use the original value
    in the contract.
    """
    id_mapping = id_mapping or {}

    def replace_ids(match: re.Match):
        match_groupdict = match.groupdict()
        resource_ids_str = str(match_groupdict["ids"])
        resource_ids = resource_ids_str.split(",")
        if match_validation:
            match_validation(resource_ids)

        resource_ids = [
            resource.replace(" ", "")
            .replace('"', "")
            .replace("'", "")
            .replace("&", "")
            .replace("{", "")
            .replace("}", "")
            for resource in resource_ids
        ]

        prefix = str(match_groupdict.get("prefix", ""))
        suffix = str(match_groupdict.get("suffix", ""))

        mapped_resource_ids = list()
        for resource_id in resource_ids:
            mapped_tag_id = id_mapping.get(resource_id)
            if not mapped_tag_id:
                log.info(
                    f"Did not find mapped {resource_type} id for {resource_id}."
                    f" Using original id."
                )
                mapped_resource_ids.append("'" + resource_id + "'")
            else:
                mapped_resource_ids.append("'" + mapped_tag_id + "'")

        return prefix + ", ".join(mapped_resource_ids) + suffix

    contractdata = re.sub(pattern=id_regex, repl=replace_ids, string=contractdata)

    return contractdata


def create_mock_message_queue(
    sample_message_file: str = "",
    yield_message_range: int = 3,
    matched_message_sleep: int = 1,
    while_loop_sleep: int = 1,
    sample_message: Any = None,
) -> Mock:
    """
    This mocks a kafka consumer, returning a mocked poller
    Rather than overriding the poll function to a mock function, it is
    set to be a generator which is instantiated and then yields the
    desired responses for the kafka message queue mock.
    :param sample_message_file: file path to sample kafka message file
    :param yield_message_range: number of matched messages to return
    :param matched_message_sleep: sleep time between match messages
    :param while_loop_sleep: sleep time between None messages
    :param sample_message: a json message to return. Overrides the
    sample_message_file
    """
    if sample_message is None:
        with open(sample_message_file, encoding="utf-8") as file:
            sample_message = file.read()

    poller = Mock()
    message_response_mock = Mock()
    message_response_decode_mock = Mock()
    message_response_decode_mock.decode.return_value = sample_message
    message_response_mock.error.return_value = False
    message_response_mock.value.return_value = message_response_decode_mock

    def mock_message_queue():
        for _ in range(yield_message_range):
            yield message_response_mock
        time.sleep(matched_message_sleep)
        while True:
            # add sleep here to slow down infinite while loop
            time.sleep(while_loop_sleep)
            yield None

    poller.poll.side_effect = mock_message_queue()
    return poller


def _validate_clu_resource_syntax(resource_ids: List[str]) -> None:
    # https://regex101.com/r/fqYUc5/1/
    clu_syntax_pattern = r"(['\"]+&\{[\w\d]*\}['\"]+)"

    # to account for cases where the resource name is hardcoded
    # https://regex101.com/r/JFZFyV/1
    hardcoded_pattern = r"(['\"]+[\w\d]*['\"]+)"

    for resource in resource_ids:
        if not re.search(clu_syntax_pattern, resource) and not re.search(
            hardcoded_pattern, resource
        ):
            raise ValueError(
                f"Resource syntax is invalid, got {resource} but should be in the format "
                f"'&{{resource_id}}' or 'resource_id'."
            )
