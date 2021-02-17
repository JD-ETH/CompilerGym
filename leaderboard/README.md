# CompilerGym Leaderboards

See [CONTRIBUTING](/CONTRIBUTING.md) for instructions on how to add your own
submission to this document.

## LLVM Codesize

Use `gym.make("llvm-v0", reward="IrInstructionCountOz")`, test set `cBench-v0`

|   | Machine | Mean Walltime | Geomean Improvement |
| --------- | --- | --------- | -- |
| [Random search (30 sec)](llvm_codesize/random_search.md) | 12-Core AMD Ryzen 9 3900X, 32GB RAM | 1.21s (1.12s std) | 1.201x (1.021 gsd) |
