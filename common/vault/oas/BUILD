python_library(
   name = "configuration",
   srcs = [
       "configuration.py"
   ],
   visibility = ["PUBLIC"],
   deps = [
        "//third_party/python3:six"
   ]
)

python_library(
   name = "rest",
   srcs = [
       "rest.py"
   ],
   visibility = ["PUBLIC"],
   deps = [
        "//third_party/python3:six"
   ]
)

python_library(
    name = "api_client",
    srcs = ["__init__.py", "api_client.py"],
    visibility = ["PUBLIC"],
    deps = [
        "//third_party/python3:certifi",
        "//third_party/python3:six",
        "//third_party/python3:urllib3",
        "//common/vault/oas/models:models",
        ":configuration",
        ":rest"
    ]
)
