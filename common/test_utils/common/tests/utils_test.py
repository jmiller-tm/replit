# standard libs
from unittest import TestCase

# common
import common.test_utils.common.utils as utils
from common.python.file_utils import load_file_contents

example_contract_path = "common/test_utils/common/tests/input/example_contract.py"
expected_output_calendars_replaced = (
    "common/test_utils/common/tests/output/contract_calendars_replaced.py"
)


class CommonUtilsTest(TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.example_contract = load_file_contents(example_contract_path)
        return super().setUp()

    def test_replace_calendar_ids_in_contract(self):

        expected_output = load_file_contents(expected_output_calendars_replaced)
        calendar_mapping = {
            "CALENDAR_1": "CALENDAR_1_REPLACED",
            "CALENDAR_2": "CALENDAR_2_REPLACED",
            "CALENDAR_3": "CALENDAR_3_REPLACED",
        }
        result = utils.replace_calendar_ids_in_contract(
            self.example_contract,
            calendar_mapping,
        )
        self.assertEqual(result, expected_output)

    def test_replace_calendar_ids_in_contract_log_raised(self):

        calendar_mapping = {
            "CALENDAR_1": "CALENDAR_1_REPLACED",
            "CALENDAR_2": "CALENDAR_2_REPLACED",
        }

        with self.assertLogs(level="INFO") as log:
            utils.replace_calendar_ids_in_contract(
                self.example_contract,
                calendar_mapping,
            )
        self.assertEqual(len(log.output), 2)
        self.assertIn(
            f"Did not find mapped calendar id for CALENDAR_3." f" Using original id.",
            log.output[0],
        )
        self.assertIn(
            f"Did not find mapped calendar id for CALENDAR_3." f" Using original id.",
            log.output[1],
        )

    def test_validate_clu_resource_syntax_catches_invalid_syntax(self):
        test_cases = [
            {
                "description": "Singe resource, missing &",
                "input": [r"'{SOME_TEXT}'"],
                "failed_resource": r"'{SOME_TEXT}'",
            },
            {
                "description": "Multi resource, missing &",
                "input": [r"'{SOME_TEXT1}'", r"'&{SOME_TEXT2}'", r"'&{SOME_TEXT3}'"],
                "failed_resource": r"'{SOME_TEXT1}'",
            },
            {
                "description": "Singe resource, missing {",
                "input": [r"'&SOME_TEXT}'"],
                "failed_resource": r"'&SOME_TEXT}'",
            },
            {
                "description": "Multi resource, missing {",
                "input": [r"'&SOME_TEXT1}'", r"'&{SOME_TEXT2}'", r"'&{SOME_TEXT3}'"],
                "failed_resource": r"'&SOME_TEXT1}'",
            },
            {
                "description": "Singe resource, missing '",
                "input": [r"&{SOME_TEXT}'"],
                "failed_resource": r"&{SOME_TEXT}'",
            },
            {
                "description": "Multi resource, missing '",
                "input": [r"'&{SOME_TEXT1}'", r"&{SOME_TEXT2}'", r"'&{SOME_TEXT3}'"],
                "failed_resource": r"&{SOME_TEXT2}'",
            },
            {
                "description": "Singe resource, missing }",
                "input": [r"'&{SOME_TEXT'"],
                "failed_resource": r"'&{SOME_TEXT'",
            },
            {
                "description": "Multi resource, missing }",
                "input": [r"'&{SOME_TEXT1}'", r"'&{SOME_TEXT2'", r"'&{SOME_TEXT3}'"],
                "failed_resource": r"'&{SOME_TEXT2'",
            },
            {
                "description": "Singe resource, not clu syntax",
                "input": ["'SOME_TEXT"],
                "failed_resource": "'SOME_TEXT",
            },
            {
                "description": "Multi resource, not clu syntax",
                "input": ["'SOME_TEXT1'", "'SOME_TEXT2", "'SOME_TEXT3'"],
                "failed_resource": "'SOME_TEXT2",
            },
        ]

        for test_case in test_cases:
            with self.assertRaises(ValueError) as e:
                utils._validate_clu_resource_syntax(test_case["input"])
            failed_resource = test_case["failed_resource"]
            self.assertEqual(
                str(e.exception),
                f"Resource syntax is invalid, got {failed_resource} but should be in the format "
                f"'&{{resource_id}}' or 'resource_id'.",
                test_case["description"],
            )

    def test_validate_clu_resource_syntax_valid_syntax(self):
        test_cases = [
            {
                "description": "Singe resource, clu syntax",
                "input": [r"'&{SOME_TEXT}'"],
            },
            {
                "description": "Multi resource, clu syntax",
                "input": [r"'&{SOME_TEXT1}'", r"'&{SOME_TEXT2}'", r"'&{SOME_TEXT3}'"],
            },
            {
                "description": "Singe resource, not clu syntax",
                "input": ["'SOME_TEXT'"],
            },
            {
                "description": "Multi resource, not clu syntax",
                "input": ["'SOME_TEXT1'", '"SOME_TEXT2"', "'SOME_TEXT3'"],
            },
        ]

        for test_case in test_cases:
            try:
                utils._validate_clu_resource_syntax(test_case["input"])
            except ValueError:
                self.fail(f"test case raised a ValueError unexpectedly.")
