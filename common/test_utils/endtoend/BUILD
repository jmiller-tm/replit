filegroup(
    name = "config",
    srcs = ["config.json"],
    visibility = [
        "PUBLIC"
    ]
)

python_library(
    name = "accounts_helper",
    srcs = ["accounts_helper.py"],
    deps = [
        ":kafka_helper"
    ],
    visibility = ["PUBLIC"],
)

python_library(
    name = "contract_modules_helper",
    srcs = ["contract_modules_helper.py"],
    deps = [
        "//common/python:file_utils"
    ],
    visibility = ["PUBLIC"],
)

python_library(
    name = "contracts_helper",
    srcs = ["contracts_helper.py"],
    visibility = ["PUBLIC"],
    resources = [ 
        "//internal_accounts:all_internal_products",
    ],
    deps= [
        "//common/python:file_utils",
        "//third_party/python3:dateutil",
        "//third_party/python3:pyyaml",
        "//third_party/python3:requests",
    ]
)

python_library(
    name = "core_api_helper",
    srcs = ["core_api_helper.py"],
    visibility = ["PUBLIC"],
)

python_library(
    name = "schedule_helper",
    srcs = ["schedule_helper.py"],
    deps = [
        ":kafka_helper"
    ],    
    visibility = ["PUBLIC"],
)

python_library(
    name = "kafka_helper",
    srcs = ["kafka_helper.py"],
    visibility = ["PUBLIC"],
    deps = [ 
        "//common/kafka:kafka"
    ]
)

python_library(
    name = "balances",
    srcs = ["balances.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":core_api_helper",
        ":kafka_helper",
        "//common/test_utils/common:balance_helpers"
    ]
)

python_library(
    name = "data_loader_helper",
    srcs = ["data_loader_helper.py"],
    deps = [
        ":kafka_helper",
        "//common/test_utils/common:date_helper",
        "//third_party/python3:pyyaml"
    ],
    visibility = [
        "PUBLIC"
    ]
)

python_test(
    name = "test_data_loader_helper",
    srcs = ["test_data_loader_helper.py"],
    deps = [
        ":data_loader_helper",
    ],
    labels = ["unit"],
)

python_library(
    name = "helper",
    srcs = ["helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":config",
        "//common/vault:environment",
        "//third_party/python3:requests"
    ]
)

python_library(
    name = "postings",
    srcs = ["postings.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":kafka_helper",
        "//common/test_utils/postings:override_classes",
        "//common/test_utils/postings:posting_classes",
        "//common/test_utils/postings:postings_helper",
    ]
)

python_library(
    name = "workflows_api_helper",
    srcs = ["workflows_api_helper.py"],
    visibility = ["PUBLIC"],
)

python_library(
    name = "workflows_helper",
    srcs = ["workflows_helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        "//third_party/python3:pyyaml",
        "//third_party/python3:jsonpath_ng",
        ":helper",
        "//common/test_utils/performance/data_objects:data_objects"
    ]
)

python_library(
    name = "supervisors_helper",
    srcs = ["supervisors_helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        "//common/test_utils/endtoend:helper",
        "//common/test_utils/common:utils"
    ]
)

python_library(
    name = "xpl_helper",
    srcs = ["xpl_helper.py"],
    visibility = ["PUBLIC"],
    deps = [
        ":helper"
    ]
)

python_library(
    name = "endtoend",
    srcs = ["__init__.py"],
    visibility = [
        "PUBLIC"
    ],
    deps = [
        ":accounts_helper",
        ":balances",
        ":contracts_helper",
        ":contract_modules_helper",
        ":core_api_helper",
        ":data_loader_helper",
        ":helper",
        ":kafka_helper",
        ":postings",
        ":schedule_helper",
        ":supervisors_helper",
        ":workflows_helper",
        ":workflows_api_helper",
        ":xpl_helper",
        "//common/vault:environment",
        "//common/test_utils/common:balance_helpers",
    ]
)
