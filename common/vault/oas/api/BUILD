filegroup(
    name="all_clients",
    srcs=glob(["*.py"]),
    visibility = ["PUBLIC"]
)

python_library(
    name = "clients",
    visibility = ["PUBLIC"],
    srcs = [
        ":all_clients"
    ],
    deps = [
        "//common/vault/oas:api_client"
    ]
)
