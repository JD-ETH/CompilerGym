# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Tests for action space determinism."""
import hashlib

import pytest

from compiler_gym.envs import LlvmEnv
from tests.test_main import main

pytest_plugins = ["tests.pytest_plugins.llvm"]

ACTION_REPTITION_COUNT = 50


@pytest.mark.skip(reason="github.com/facebookresearch/CompilerGym/issues/46")
@pytest.mark.parametrize(
    "benchmark_name",
    [
        "benchmark://cBench-v1/adpcm",
        "benchmark://cBench-v1/bitcount",
        "benchmark://cBench-v1/blowfish",
        "benchmark://cBench-v1/bzip2",
        "benchmark://cBench-v1/ghostscript",
        "benchmark://cBench-v1/gsm",
        "benchmark://cBench-v1/ispell",
        "benchmark://cBench-v1/jpeg-c",
        "benchmark://cBench-v1/jpeg-d",
        "benchmark://cBench-v1/patricia",
        "benchmark://cBench-v1/rijndael",
        "benchmark://cBench-v1/stringsearch",
        "benchmark://cBench-v1/stringsearch2",
        "benchmark://cBench-v1/susan",
        "benchmark://cBench-v1/tiff2bw",
        "benchmark://cBench-v1/tiff2rgba",
        "benchmark://cBench-v1/tiffdither",
        "benchmark://cBench-v1/tiffmedian",
    ],
)
def test_gvn_sink_non_determinism(env: LlvmEnv, benchmark_name: str):
    """Regression test for -gvn-sink non-determinism.
    See: https://github.com/facebookresearch/CompilerGym/issues/46
    """
    env.observation_space = "Ir"

    checksums = set()
    for i in range(1, ACTION_REPTITION_COUNT + 1):
        env.reset(benchmark=benchmark_name)
        ir, _, done, _ = env.step(env.action_space.names.index("-gvn-sink"))
        assert not done
        sha1 = hashlib.sha1()
        sha1.update(ir.encode("utf-8"))
        checksums.add(sha1.hexdigest())

        if len(checksums) != 1:
            pytest.fail(
                f"Repeating the -gvn-sink action {i} times on {benchmark_name} "
                "produced different states"
            )


if __name__ == "__main__":
    main()
