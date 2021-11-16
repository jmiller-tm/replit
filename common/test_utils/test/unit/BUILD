python_test(
    name = "test_balances",
    srcs = ["test_balances.py"],
    data = [
        # This shouldn't really be needed, but will be fixed when we restructure
        # The e2e test helpers
        "//common/test_utils/endtoend:config"
    ],
    deps = [
        "//common/test_utils/endtoend"
    ],
    labels = ["unit"],
)

python_test(
    name = "test_schedule_helper",
    srcs = ["test_schedule_helper.py"],
    data = [
        # This shouldn't really be needed, but will be fixed when we restructure
        # The e2e test helpers
        "//common/test_utils/endtoend:config"
    ],
    deps = [
        "//common/test_utils/endtoend"
    ],
    labels = ["unit"],
)

python_test(
    name = "test_workflows_helper",
    srcs = ["test_workflows_helper.py"],
    data = [
        # This shouldn't really be needed, but will be fixed when we restructure
        # The e2e test helpers
        "//common/test_utils/common:utils",
        "//common/test_utils/endtoend:config",
        "//common/test_utils/test/unit/input:wf_message_event"
    ],
    deps = [
        "//third_party/python3:pyyaml",
        "//common/test_utils/endtoend"
    ],
    labels = ["unit"],
)

python_test(
    name = "test_supervisors_helper",
    srcs = ["test_supervisors_helper.py"],
    data = [
        # This shouldn't really be needed, but will be fixed when we restructure
        # The e2e test helpers
        "//common/test_utils/endtoend:config",
        "//common/test_utils/test/unit/input:normal_plan_associations",
        "//common/test_utils/test/unit/input:multi_plan_associations",
    ],
    deps = [
         "//common/test_utils/endtoend"
    ],
    labels = ["unit"],
)