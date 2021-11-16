python_library(
    name = "performance_helper",
    srcs = ["performance_helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":schedules_helper",
        ":test_types",
        "//common/python:file_utils",
        "//common/test_utils/common:date_helper",
        "//common/test_utils/endtoend",
        "//common/test_utils/contracts/simulation/common:helper",
        "//common/test_utils/contracts/simulation/mock_product:empty_contract",
        "//common/test_utils/contracts/simulation:simulation_test_utils",
        "//common/test_utils/performance/data_objects:data_objects",
        "//common/test_utils/postings:posting_classes",
        "//common/test_utils/postings:postings_helper",
        ":prometheus_api_helper",
        "//third_party/python3:pyyaml",
        "//third_party/python3:requests"
    ]
)

python_library(
    name = "schedules_helper",
    srcs = ["schedules_helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        "//common/python:file_utils",
        "//common/test_utils/common:date_helper",
        "//common/test_utils/endtoend",
    ]
)

python_library(
    name="test_types",
    srcs=["test_types.py"],
    visibility = ["PUBLIC"],
)

filegroup(
    name = "performance_queries",
    srcs = ["performance_queries.json"],
    visibility = [
        "PUBLIC"
    ]
)

python_library(
    name = "prometheus_api_helper",
    srcs = [
        "prometheus_api_helper.py",
    ],
    visibility = ["PUBLIC"],
    deps = [
        ":test_types",
        "//common/python:resources",
        "//common/test_utils/endtoend",
    ],
    resources = [
        ":performance_queries",
    ]
)

python_binary(
    name = "prometheus_api_helper_bin",
    main = "prometheus_api_helper.py",
    visibility = ["PUBLIC"],
    data = [
        "//common/test_utils/endtoend:config",
    ],
    deps = [
        ":test_types",
        "//common/python:resources",
        "//common/test_utils/endtoend",
    ],
    resources = [
        ":performance_queries",
    ]
)
