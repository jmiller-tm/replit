python_test(
    name = "test_contract_module_account",
    srcs = ["test_contract_module_account.py"],
    data = [
        "//common/test_utils/common/contract_modules_examples:contract_module",
        "//common/test_utils/common/contract_modules_examples:contract_module_2",
        "//common/test_utils/common/contract_modules_examples:full_contract_with_shared_function",
        "//common/test_utils/endtoend:config"
    ],
    deps = [
        "//common/test_utils/endtoend",
        "//third_party/python3:dateutil"
    ],
    labels = ["e2e"],
)
