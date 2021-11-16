python_test(
    name = "test_contract_modules",
    srcs = ["test_contract_modules.py"],
    data = [
        "//common/test_utils/common/contract_modules_examples:contract_module"
    ],
    deps = [
        "//common/test_utils/contracts/unit:common",
    ],
    labels = ["unit"],
)

python_test(
    name = "test_contract_with_shared_function",
    srcs = ["test_contract_with_shared_function.py"],
    data = [
        "//common/test_utils/common/contract_modules_examples:full_contract_with_shared_function",
        "//common/test_utils/common/contract_modules_examples:contract_module"
    ],
    deps = [
        "//common/test_utils/contracts/unit:common",
    ],
    labels = ["unit"],
)