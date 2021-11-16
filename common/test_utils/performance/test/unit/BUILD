python_test(
    name = "test_performance_helper",
    srcs = ["test_performance_helper.py"],
    data = [
        # This shouldn't really be needed, but will be fixed when we restructure
        # The e2e test helpers
        "//common/test_utils/endtoend:config",
        "//common/test_utils/performance/test/unit/output:test_data",
        "//common/test_utils/performance/test/unit/input:test_data",
    ],
    deps = [
        "//third_party/python3:requests",
        "//third_party/python3:pyyaml",
        "//common/test_utils/common:utils",
        "//common/test_utils/endtoend",
        "//common/test_utils/performance/test/unit/output:test_objects",
        "//common/test_utils/performance/test/unit/input:generate_postings_sim_input",
        "//common/test_utils/performance:performance_helper",
    ],
    labels = ["unit"],
)

python_test(
    name = "test_prometheus_api_helper",
    srcs = ["test_prometheus_api_helper.py"],
    data = [
        "//common/test_utils/endtoend:config",
    ],
    deps = [
        "//common/test_utils/endtoend",
        "//common/test_utils/performance:prometheus_api_helper",
        "//third_party/python3:dateutil"
    ],
    labels = ["unit"],
)

python_test(
    name = "test_schedules_helper",
    srcs = ["test_schedules_helper.py"],
    data = [],
    deps = [
        "//common/test_utils/endtoend",
        "//common/test_utils/performance:schedules_helper"
    ],
    labels = ["unit"],
)
