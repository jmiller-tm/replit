filegroup(
    name="all_models",
    srcs=glob(["*.py"]),
    visibility = ["PUBLIC"]
)

python_library(
    name = "models",
    visibility = ["PUBLIC"],
    srcs=[
        "//third_party/python3:six",
        ":all_models"
    ]
)
