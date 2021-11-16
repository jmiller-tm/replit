# Copyright @ 2021 Thought Machine Group Limited. All rights reserved.
# standard libs
import logging
import os
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from typing import Dict, List, OrderedDict

# third party

# common
from common.test_utils import endtoend
from common.test_utils.common.date_helper import extract_date
from common.test_utils.endtoend.core_api_helper import (
    batch_get_account_schedule_tags,
    get_account_schedules,
)
from common.test_utils.endtoend.schedule_helper import (
    wait_for_schedule_operation_events,
)

log = logging.getLogger(__name__)
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(asctime)s.%(msecs)03d - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def skip_previous_schedules_in_schedule_group(
    schedule_tag: str,
    schedule_group: OrderedDict[int, List],
    schedule_next_run_times: Dict[str, datetime],
) -> None:
    """
    Skips all schedules within a schedule group that are required to allow execution of the next
    schedule controlled by schedule_tag.
    (E.g. if a schedule group consists of 3 schedules A, B and C and schedule_tag controls schedule
    C, then schedules A and B will be skipped to match the current next runtime of schedule C.
    Alternatively, if schedule_tag controls schedule A or some other schedule that is not part of
    the group, then no schedules will be skipped.)
    """
    e2e_tag_id = endtoend.testhandle.schedule_tag_ids_to_e2e_ids[schedule_tag]
    schedule_tags_to_skip = []
    for schedule_tags in schedule_group.values():
        if e2e_tag_id in schedule_tags and schedule_tags_to_skip:
            prev_schedule_tags_in_group = batch_get_account_schedule_tags(
                schedule_tags_to_skip
            )
            _skip_schedule_tags_to_date(
                prev_schedule_tags_in_group,
                schedule_next_run_times[e2e_tag_id],
                schedule_next_run_times,
            )
            break
        schedule_tags_to_skip.extend(schedule_tags)


def get_schedule_groups(account_schedules: Dict) -> Dict[str, OrderedDict]:
    """
    Returns a dictionary of schedule groups, their corresponding group order and related
    schedule tags.
    """
    schedule_groups: Dict[str, Dict] = {}
    for schedule_details in account_schedules.values():
        schedule_group = schedule_details.get("group")
        schedule_tags = schedule_details.get("tags")
        if schedule_group:
            group_id = schedule_group["group_id"]
            group_order = schedule_group["group_order"]
            schedule_group_mapping = schedule_groups.get(group_id)
            if schedule_group_mapping:
                schedule_group_mapping.update({group_order: schedule_tags})
            else:
                schedule_groups.update({group_id: {group_order: schedule_tags}})

    # Ensure that all schedule groups are ordered by group_order
    ordered_schedule_groups = {}
    for group_id, schedule_group in schedule_groups.items():
        ordered_schedule_group = OrderedDict(sorted(schedule_group.items()))
        ordered_schedule_groups.update({group_id: ordered_schedule_group})
    return ordered_schedule_groups


def get_schedule_tag_next_run_times(account_id: str) -> Dict[str, datetime]:
    """
    Returns a dictionary of schedule tags and the earliest next runtime of any associated
    schedules.
    """
    schedule_next_run_times = {}
    account_schedules = get_account_schedules(account_id)
    for schedule_details in account_schedules.values():
        schedule_tags = schedule_details.get("tags")
        for schedule_tag in schedule_tags:
            next_runtime = extract_date(schedule_details["next_run_timestamp"])
            if (
                not schedule_next_run_times.get(schedule_tag)
                or next_runtime < schedule_next_run_times[schedule_tag]
            ):
                schedule_next_run_times.update({schedule_tag: next_runtime})
    return schedule_next_run_times


def _skip_schedule_tags_to_date(
    schedule_tags: Dict[str, Dict],
    skip_to_date: datetime,
    schedule_next_run_times: Dict[str, datetime],
) -> None:
    """
    Set the schedule tags in schedule_tags to skipped and their test_pause_at_timestamp to
    skip_to_date if the current next run time is before skip_to_date.
    """
    tags_moved = []
    for prev_tag in schedule_tags:
        if schedule_next_run_times[prev_tag] < skip_to_date:
            log.info(
                f"Skipping schedule(s) for {prev_tag} from {schedule_next_run_times[prev_tag]} "
                f"to {skip_to_date}..."
            )
            # Ensure that tzinfo is set so that isoformat() returns a format that Vault accepts
            if skip_to_date.tzinfo is None:
                skip_to_date = skip_to_date.replace(tzinfo=timezone.utc)
            endtoend.core_api_helper.update_account_schedule_tag(
                account_schedule_tag_id=prev_tag,
                schedule_status_override_start_timestamp=datetime.min.replace(
                    tzinfo=timezone.utc
                ).isoformat(),
                schedule_status_override_end_timestamp=datetime.max.replace(
                    tzinfo=timezone.utc
                ).isoformat(),
                schedule_status_override="ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_SKIPPED",
                test_pause_at_timestamp=skip_to_date.isoformat(),
            )
            tags_moved.append(prev_tag)
    if tags_moved:
        # Set the time element to start of day to ensure any schedule for that day is included
        # as we support a maximum frequency of DAILY
        skip_to_date = skip_to_date + relativedelta(
            hour=0, minute=0, second=0, microsecond=0
        )
        wait_for_schedule_operation_events(
            tag_names=tags_moved,
            use_e2e_mapping=False,
            wait_for_timestamp=skip_to_date,
            inter_message_timeout=0,
            matched_message_timeout=0,
        )
