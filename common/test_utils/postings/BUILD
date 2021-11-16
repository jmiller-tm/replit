python_library(
    name = "override_classes",
    srcs = ["override_classes.py"],
    visibility = ["PUBLIC"],
)

python_library(
    name = "posting_classes",
    srcs = ["posting_classes.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":override_classes"
    ]
)

python_library(
    name = "postings_helper",
    srcs = ["postings_helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":override_classes",
        ":posting_classes",
    ]
)
