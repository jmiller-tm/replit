# Copyright @ 2021 Thought Machine Group Limited. All rights reserved.
# standard libs
import time
from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import Mock, call, patch

# common
from common.test_utils import endtoend
from common.test_utils.performance import schedules_helper
from common.test_utils.performance.schedules_helper import (
    _skip_schedule_tags_to_date,
    get_schedule_groups,
    get_schedule_tag_next_run_times,
    skip_previous_schedules_in_schedule_group,
)


MOCK_ACCOUNT_SCHEDULES = {
    "ACCRUE_INTEREST": {
        "id": "adda847e-602f-4d26-aa8c-ff36217d5fdd",
        "name": "0_CF4LL7NXC1R561TI9VZRS3FGS1JZPZXQ6_ACCRUE_INTEREST_536802",
        "display_name": "ACCRUE_INTEREST for 0_CF4LL7NXC1R561TI9VZRS3FGS1JZPZXQ6",
        "status": "SCHEDULE_STATUS_ENABLED",
        "create_timestamp": "2021-09-07T19:40:26Z",
        "start_timestamp": "2021-05-20T09:00:00Z",
        "end_timestamp": None,
        "next_run_timestamp": "2021-05-21T00:00:00Z",
        "disabled_timestamp": None,
        "time_expression": "0 0 0 * * * *",
        "timezone": "UTC",
        "tags": ["PAUSED_ACCRUE_INTEREST_ba0119d2-37fd-48f9-ac89-716cf2e5119f"],
        "group": {
            "group_id": "39be6e13-6b8a-4ad7-9624-fcc2079147f2",
            "group_order": 0,
        },
    },
    "PAYMENT_DUE": {
        "id": "c494445e-262d-4363-aa6e-f91a68b7306f",
        "name": "0_CF4LL7NXC1R561TI9VZRS3FGS1JZPZXQ6_PAYMENT_DUE_536802",
        "display_name": "PAYMENT_DUE for 0_CF4LL7NXC1R561TI9VZRS3FGS1JZPZXQ6",
        "status": "SCHEDULE_STATUS_ENABLED",
        "create_timestamp": "2021-09-07T19:40:26Z",
        "start_timestamp": "2021-05-20T09:00:00Z",
        "end_timestamp": None,
        "next_run_timestamp": "2021-07-14T00:00:01Z",
        "disabled_timestamp": None,
        "time_expression": "1 0 0 14 7 * *",
        "timezone": "UTC",
        "tags": ["PAUSED_PAYMENT_DUE_5b0524b1-6e2d-4244-8a56-c35ca2ef2f82"],
        "group": {
            "group_id": "39be6e13-6b8a-4ad7-9624-fcc2079147f2",
            "group_order": 1,
        },
    },
}

MOCK_SCHEDULE_NEXT_RUN_TIMES = {
    "tag_1": datetime(2021, 1, 10, tzinfo=timezone.utc),
    "tag_2": datetime(2021, 1, 12, tzinfo=timezone.utc),
    "tag_3": datetime(2021, 1, 14, tzinfo=timezone.utc),
}


class SchedulesHelperTest(TestCase):
    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        self._elapsed_time = time.time() - self._started_at
        # Uncomment this for timing info.
        # print('\n{} ({}s)'.format(self.id().rpartition('.')[2], round(self._elapsed_time, 2)))

    @patch.object(schedules_helper, "get_account_schedules")
    def test_get_schedule_tag_next_run_times(self, get_account_schedules: Mock):
        account_id = "mock"
        get_account_schedules.return_value = MOCK_ACCOUNT_SCHEDULES
        expected_result = {
            "PAUSED_ACCRUE_INTEREST_ba0119d2-37fd-48f9-ac89-716cf2e5119f": datetime(
                2021, 5, 21, 0, 0, tzinfo=timezone.utc
            ),
            "PAUSED_PAYMENT_DUE_5b0524b1-6e2d-4244-8a56-c35ca2ef2f82": datetime(
                2021, 7, 14, 0, 0, 1, tzinfo=timezone.utc
            ),
        }
        result = get_schedule_tag_next_run_times(account_id)
        self.assertEqual(result, expected_result)

    def test_get_schedule_groups(self):
        expected_result = {
            "39be6e13-6b8a-4ad7-9624-fcc2079147f2": {
                0: ["PAUSED_ACCRUE_INTEREST_ba0119d2-37fd-48f9-ac89-716cf2e5119f"],
                1: ["PAUSED_PAYMENT_DUE_5b0524b1-6e2d-4244-8a56-c35ca2ef2f82"],
            }
        }
        result = get_schedule_groups(MOCK_ACCOUNT_SCHEDULES)
        self.assertEqual(result, expected_result)

    @patch(
        "common.test_utils.endtoend.testhandle.schedule_tag_ids_to_e2e_ids",
        {"tag_1": "tag_1", "tag_2": "tag_2", "tag_3": "tag_3"},
    )
    @patch.object(schedules_helper, "batch_get_account_schedule_tags")
    @patch.object(schedules_helper, "_skip_schedule_tags_to_date")
    def test_skip_previous_schedules_in_schedule_group(
        self,
        mock_skip_schedule_tags_to_date: Mock,
        mock_batch_get_account_schedule_tags: Mock,
    ):
        mock_schedule_group = {0: ["tag_1"], 1: ["tag_2"], 2: ["tag_3"]}
        mock_prev_schedule_tags_in_group = {
            "tag_1": {},
            "tag_2": {"tag_1": None},
            "tag_3": {"tag_1": None, "tag_2": None},
        }

        batch_get_account_schedule_tags_expected_calls = {
            "tag_1": [],
            "tag_2": [call(["tag_1"])],
            "tag_3": [call(["tag_1"]), call(["tag_1", "tag_2"])],
        }
        skip_schedule_tags_to_date_expected_calls = {
            "tag_1": [],
            "tag_2": [
                call(
                    {"tag_1": None},
                    datetime(2021, 1, 12, tzinfo=timezone.utc),
                    MOCK_SCHEDULE_NEXT_RUN_TIMES,
                )
            ],
            "tag_3": [
                call(
                    {"tag_1": None, "tag_2": None},
                    datetime(2021, 1, 14, tzinfo=timezone.utc),
                    MOCK_SCHEDULE_NEXT_RUN_TIMES,
                )
            ],
        }

        for tag in ["tag_1", "tag_2", "tag_3"]:
            mock_batch_get_account_schedule_tags.return_value = (
                mock_prev_schedule_tags_in_group[tag]
            )
            skip_previous_schedules_in_schedule_group(
                tag, mock_schedule_group, MOCK_SCHEDULE_NEXT_RUN_TIMES
            )
            mock_batch_get_account_schedule_tags.assert_has_calls(
                batch_get_account_schedule_tags_expected_calls[tag]
            )
            mock_skip_schedule_tags_to_date.assert_has_calls(
                skip_schedule_tags_to_date_expected_calls[tag]
            )

    @patch.object(schedules_helper.log, "info")
    @patch.object(endtoend.core_api_helper, "update_account_schedule_tag")
    @patch.object(schedules_helper, "wait_for_schedule_operation_events")
    def test_skip_schedule_tags_to_date_tag_2(
        self,
        mock_wait_for_schedule_operation_events: Mock,
        mock_update_account_schedule_tag: Mock,
        mock_log_info: Mock,
    ):
        mock_prev_schedule_tags_in_group = {"tag_1": None}
        mock_skip_to_date = datetime(2021, 1, 12, tzinfo=timezone.utc)
        _skip_schedule_tags_to_date(
            mock_prev_schedule_tags_in_group,
            mock_skip_to_date,
            MOCK_SCHEDULE_NEXT_RUN_TIMES,
        )
        mock_log_info.assert_has_calls(
            [
                call(
                    "Skipping schedule(s) for tag_1 from 2021-01-10 00:00:00+00:00 to 2021-01-12 "
                    "00:00:00+00:00..."
                )
            ]
        )
        mock_update_account_schedule_tag.assert_has_calls(
            [
                call(
                    account_schedule_tag_id="tag_1",
                    schedule_status_override="ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_"
                    "SKIPPED",
                    schedule_status_override_start_timestamp="0001-01-01T00:00:00+00:00",
                    schedule_status_override_end_timestamp="9999-12-31T23:59:59.999999+00:00",
                    test_pause_at_timestamp="2021-01-12T00:00:00+00:00",
                )
            ]
        )
        mock_wait_for_schedule_operation_events.assert_has_calls(
            [
                call(
                    inter_message_timeout=0,
                    matched_message_timeout=0,
                    tag_names=["tag_1"],
                    use_e2e_mapping=False,
                    wait_for_timestamp=datetime(2021, 1, 12, 0, 0, tzinfo=timezone.utc),
                )
            ]
        )

    @patch.object(schedules_helper.log, "info")
    @patch.object(endtoend.core_api_helper, "update_account_schedule_tag")
    @patch.object(schedules_helper, "wait_for_schedule_operation_events")
    def test_skip_schedule_tags_to_date_tag_3(
        self,
        mock_wait_for_schedule_operation_events: Mock,
        mock_update_account_schedule_tag: Mock,
        mock_log_info: Mock,
    ):
        mock_prev_schedule_tags_in_group = {"tag_1": None, "tag_2": None}
        mock_skip_to_date = datetime(2021, 1, 14, tzinfo=timezone.utc)
        _skip_schedule_tags_to_date(
            mock_prev_schedule_tags_in_group,
            mock_skip_to_date,
            MOCK_SCHEDULE_NEXT_RUN_TIMES,
        )
        mock_log_info.assert_has_calls(
            [
                call(
                    "Skipping schedule(s) for tag_1 from 2021-01-10 00:00:00+00:00 to 2021-01-14 "
                    "00:00:00+00:00..."
                ),
                call(
                    "Skipping schedule(s) for tag_2 from 2021-01-12 00:00:00+00:00 to 2021-01-14 "
                    "00:00:00+00:00..."
                ),
            ]
        )
        mock_update_account_schedule_tag.assert_has_calls(
            [
                call(
                    account_schedule_tag_id="tag_1",
                    schedule_status_override="ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_"
                    "SKIPPED",
                    schedule_status_override_start_timestamp="0001-01-01T00:00:00+00:00",
                    schedule_status_override_end_timestamp="9999-12-31T23:59:59.999999+00:00",
                    test_pause_at_timestamp="2021-01-14T00:00:00+00:00",
                ),
                call(
                    account_schedule_tag_id="tag_2",
                    schedule_status_override="ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_"
                    "SKIPPED",
                    schedule_status_override_start_timestamp="0001-01-01T00:00:00+00:00",
                    schedule_status_override_end_timestamp="9999-12-31T23:59:59.999999+00:00",
                    test_pause_at_timestamp="2021-01-14T00:00:00+00:00",
                ),
            ]
        )
        mock_wait_for_schedule_operation_events.assert_has_calls(
            [
                call(
                    inter_message_timeout=0,
                    matched_message_timeout=0,
                    tag_names=["tag_1", "tag_2"],
                    use_e2e_mapping=False,
                    wait_for_timestamp=datetime(2021, 1, 14, 0, 0, tzinfo=timezone.utc),
                )
            ]
        )
