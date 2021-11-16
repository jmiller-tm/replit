python_library(
    name = "helper",
    srcs = ["helper.py"],
    resources = [
        "//internal_accounts:testing_internal_asset_account_contract",
        "//internal_accounts:testing_internal_liability_account_contract",
        "//common/test_utils/contracts/simulation/mock_product:empty_contract",
    ],
    visibility = ["PUBLIC"],
    deps = [
        "//common/python:file_utils",
        "//common/test_utils/postings:override_classes",
        "//common/test_utils/postings:posting_classes",
        "//common/test_utils/contracts/simulation/common:helper",
        "//common/test_utils/contracts/simulation/data_objects:data_objects",
        "//common/test_utils/contracts/simulation/data_objects/events:all_simulation_events",
        "//common/test_utils/contracts/unit:types_extension"
    ]
)

python_library(
    name = "vault_caller",
    srcs = ["vault_caller.py"],
    visibility = [
        "PUBLIC"
    ],
    deps = [
        "//common/python:file_utils",
        "//common/test_utils/common:utils",
        "//third_party/python3:requests",
        ":helper"
    ]
)

python_test(
    name = "vault_caller_helper_test",
    srcs = ["vault_caller_helper_test.py"],
    visibility = [
        "PUBLIC"
    ],
    data = [
        "//common/test_utils/contracts/simulation/mock_product:full_contract",
        "//common/test_utils/contracts/simulation/mock_product:full_contract_updated_version",
        "//common/test_utils/contracts/simulation/mock_product:supervised_savings_deposit_account",
        "//common/test_utils/contracts/simulation/mock_product:supervised_savings_deposit_account_with_contract_modules",
        "//common/test_utils/contracts/simulation/mock_product:supervised_checking_account",
        "//common/test_utils/contracts/simulation/mock_product:supervised_checking_account_with_contract_modules",
        "//common/test_utils/contracts/simulation/mock_product:supervised_youth_account",
        "//common/test_utils/contracts/simulation/mock_product:supervisor_contract",
        "//common/test_utils/common/contract_modules_examples:contract_module",
        "//common/test_utils/common/contract_modules_examples:contract_module_2",
        "//common/test_utils/common/contract_modules_examples:full_contract_with_shared_function",
        ":test_config"
    ],
    deps = [
        ":vault_caller",
        "//common/test_utils/common:utils",
        "//common/test_utils/contracts/simulation:simulation_test_utils",
        ":simulation_test_utils",
        ":helper",
        "//common/test_utils/contracts/simulation/data_objects:data_objects",
        "//common/test_utils/contracts/unit:types_extension",
    ],
    tags = ["simulation"]
)
python_library(
    name = "simulation_test_utils",
    srcs = ["simulation_test_utils.py"],
    visibility = [
        "PUBLIC"
    ],
    deps = [
        ":vault_caller",
        ":helper",
        "//common/python:file_utils",
        "//common/test_utils/common:balance_helpers",
        "//common/test_utils/common:timeseries",
        "//common/test_utils/postings:postings_helper",
        "//common/test_utils/postings:posting_classes",
        "//common/test_utils/contracts/simulation/data_objects:data_objects",
        "//third_party/python3:dateutil"
    ]
)


export_file(
    name = "backdated_simulator_response",
    src = "backdated_simulator_response"
)

export_file(
    name = "sample_simulator_response",
    src = "sample_simulator_response"
)

export_file(
    name = "sample_supervisor_response",
    src = "sample_supervisor_response"
)

python_test(
    name = "simulation_utils_test",
    srcs = ["simulation_utils_test.py"],
    visibility = [
        "PUBLIC"
    ],
    data = [
        ":backdated_simulator_response",
        ":sample_simulator_response",
        ":sample_supervisor_response"
    ],
    deps = [
        ":simulation_test_utils",
        ":helper",
        "//common/test_utils/contracts/simulation/data_objects:data_objects",
    ]
)

filegroup(
    name = "test_config",
    srcs = ["test_config.json"],
    visibility = [
        "PUBLIC"
    ]
)