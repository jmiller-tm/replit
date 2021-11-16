
python_test(
    name = "test_prometheus_api_helper",
    srcs = ["test_prometheus_api_helper.py"],
    data = [
        "//common/test_utils/endtoend:config",
    ],
    deps = [
        "//common/test_utils/endtoend",
        "//common/test_utils/performance:prometheus_api_helper",
        "//common/test_utils/performance:test_types",
        "//third_party/python3:dateutil"
    ],
    labels = ["e2e"],
)
