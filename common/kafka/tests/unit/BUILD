python_test(
    name = "test_kafka",
    srcs = ["test_kafka.py"],
    data = [
        "//common/kafka/tests/unit/input:wf_instantiation_event",
        "//common/kafka/tests/unit/input:balance_update_event",
    ],
    deps = [
        "//third_party/python3:confluent-kafka",
        "//common/test_utils/common:utils",
        "//common/test_utils/endtoend",
        "//common/kafka:kafka",
        "//common/test_utils/performance/data_objects:data_objects",
    ],
    labels = ["unit"],
)