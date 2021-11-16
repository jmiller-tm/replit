python_test(
    name = "coverage_test",
    srcs = ["coverage_test.py"],
    data = [
        ":coverage_test_contract"
    ],
    deps = [
        "//common/test_utils/contracts/unit:common",
    ],
    labels = ["unit"],
)

python_library(
    name = "coverage_test_contract",
    srcs = ["coverage_test_contract.py"],
    visibility = [
        "PUBLIC",
    ],
    deps = [],
)
