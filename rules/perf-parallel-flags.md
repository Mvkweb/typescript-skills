# perf-parallel-flags

> Scale TS 7 with `--checkers`/`--builders`; use `--singleThreaded` only to debug

## Why It Matters

TS 7 parallelizes parsing/emit automatically and type-checking via worker checkers (default 4). Large repos on many-core machines gain another 30–50% with `--checkers 8`; monorepos gain with `--builders N` under `--build`. Capping to 1 is for debugging order-dependent results or tiny CI runners, not the default.

## Bad

```bash
# 16-core machine, huge repo — leaving default workers + serial refs
tsc --noEmit
```

## Good

```bash
tsc --noEmit --checkers 8
tsc --build --builders 4 --checkers 4   # monorepo: 4 projects × 4 checkers max 16
tsc --noEmit --singleThreaded           # debug / 1-vCPU CI only
```

## See Also

- [cfg-ts7-side-by-side](cfg-ts7-side-by-side.md) - TS 7 adoption setup
- [perf-explicit-return-lib](perf-explicit-return-lib.md) - Reduce work before parallelizing it
