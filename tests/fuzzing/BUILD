# This package contains fuzzers - tests that generate random inputs.
#
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

py_test(
    name = "llvm_deterministic_action_fuzz_test",
    srcs = ["llvm_deterministic_action_fuzz_test.py"],
    deps = [
        "//compiler_gym",
        "//tests:test_main",
        "//tests/pytest_plugins:llvm",
    ],
)

py_test(
    name = "llvm_fork_env_fuzz_test",
    srcs = ["llvm_fork_env_fuzz_test.py"],
    deps = [
        "//compiler_gym",
        "//tests:test_main",
        "//tests/pytest_plugins:llvm",
    ],
)

py_test(
    name = "llvm_trajectory_replay_fuzz_test",
    srcs = ["llvm_trajectory_replay_fuzz_test.py"],
    deps = [
        "//compiler_gym",
        "//tests:test_main",
        "//tests/pytest_plugins:llvm",
        "//tests/pytest_plugins:random_util",
    ],
)

py_test(
    name = "llvm_validate_fuzz_test",
    srcs = ["llvm_validate_fuzz_test.py"],
    deps = [
        "//compiler_gym",
        "//tests:test_main",
        "//tests/pytest_plugins:llvm",
    ],
)
