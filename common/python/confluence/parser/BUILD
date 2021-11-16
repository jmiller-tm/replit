subinclude("//tools/defs:confluence")

python_library(
    name = "parser",
    srcs = [
        "__init__.py",
    ],
    visibility = ["PUBLIC"],
    deps = [
        "//common/python/confluence/parser/extensions",
        "//third_party/python3:markdown",
        "//third_party/python3:md2py",
    ],
)

filegroup(
    name = "tests",
    srcs = glob(["tests/*"]),
)

python_test(
    name = "parser_test",
    srcs = [
        "parser_test.py",
    ],
    resources = [":tests"],
    deps = [
        ":parser",
        "//third_party/python3:markdown",
        "//third_party/python3:md2py",
    ],
)

python_binary(
    name = "parser_bin",
    main = ":parser",
    deps = [
        "//common/python/confluence/parser/extensions",
        "//third_party/python3:markdown",
        "//third_party/python3:md2py",
    ],
)
