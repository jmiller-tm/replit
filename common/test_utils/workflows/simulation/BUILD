python_library(
    name = "workflows_api_client",
    srcs = ["workflows_api_client.py"],
    visibility = [
        "PUBLIC",
    ],
    deps = [
        "//third_party/python3:requests",
    ],
)

python_test(
    name = "workflows_api_client_test",
    srcs = ["workflows_api_client_test.py"],
    data = [
        #TODO(INC-3438): move the config out of endtoend
        "//common/test_utils/endtoend:config",
    ],
    tags = ["simulation"],
    visibility = [
        "PUBLIC",
    ],
    deps = [
        ":workflows_api_test_base",
        "//common/vault:environment"
    ],
)

python_library(
    name = "workflows_api_test_base",
    srcs = ["workflows_api_test_base.py"],
    visibility = [
        "PUBLIC",
    ],
    deps = [
        ":workflows_api_client",
    ],
)
