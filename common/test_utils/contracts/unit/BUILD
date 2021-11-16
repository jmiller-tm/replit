python_library(
    name = "unit_test_utils",
    srcs = ["__init__.py"],
    visibility = ["PUBLIC"],
)

python_library(
    name = "common",
    srcs = ["common.py"],
    visibility = [
        "PUBLIC",
    ],
    deps = [
        ":types_extension",
        ":unit_test_utils",
    ],
)

python_library(
    name = "types",
    srcs = ["types.py"],
    visibility = [
        "//common/test_utils/contracts/unit/...",
    ],
    deps = [
        "//third_party/python3:dateutil",
    ],
)

python_library(
    name = "types_extension",
    srcs = ["types_extension.py"],
    visibility = [
        "PUBLIC",
    ],
    deps = [
        ":types",
    ],
)
