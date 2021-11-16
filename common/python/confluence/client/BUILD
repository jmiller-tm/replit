python_library(
    name = "client",
    srcs = [
        "__init__.py",
        "exceptions.py",
    ],
    visibility = ["PUBLIC"],
    deps = [
        "//third_party/python3:requests",
    ],
)

python_test(
    name = "client_test",
    srcs = [
        "client_test.py",
    ],
    deps = [
        ":client",
        "//third_party/python3:requests_mock",
    ],
)
