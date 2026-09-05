#!/usr/bin/env python3
"""Classify tsc errors on generated examples and gate against a baseline.

Buckets per file:
  fragment — every error is name/module resolution (TS2304/TS2552 no name,
             TS2307/TS7016 no module, TS2305 no exported member). The block
             references helpers defined elsewhere in its rule; expected.
  artifact — extraction side-effects (stray `...` pseudocode tokens TS1005 at
             a `...` line, duplicate ambient identifiers). Not real bugs.
  SUSPECT  — anything else (wrong type, bad arity, bad syntax in a Good
             example). Review and fix the rule.

Usage:
    python3 analyze.py check.log                      # classify, human-readable
    python3 analyze.py check.log --emit-baseline       # print accepted-suspect list
    python3 analyze.py check.log --check-baseline baseline.txt   # CI gate:
                                                      # fail on NEW suspects

Baseline signatures are `file: TScode: message` with quoted identifiers
normalized, so wording stays stable across runs on the same toolchain.
"""
import pathlib
import re
import sys

FRAGMENT_CODES = {"2304", "2307", "2305", "2552", "7016"}
ARTIFACT_HINTS = ("...", "Duplicate identifier")

ERR = re.compile(
    r"^(?P<file>[^(]+\.ts)\((?P<line>\d+),(?P<col>\d+)\): "
    r"error TS(?P<code>\d+): (?P<msg>.*)$"
)


def signature(code: str, msg: str) -> tuple[str, str]:
    msg = re.sub(r"'[^']*'", "'?'", msg)
    return f"TS{code}", msg


def load(path: pathlib.Path) -> dict[str, list[tuple[str, str]]]:
    per_file: dict[str, list[tuple[str, str]]] = {}
    for line in path.read_text().splitlines():
        m = ERR.match(line.strip())
        if not m:
            continue
        name = pathlib.Path(m.group("file")).name
        if name == "ambient.d.ts":
            continue
        per_file.setdefault(name, []).append((m.group("code"), m.group("msg")))
    return per_file


def classify(errs: list[tuple[str, str]]) -> str:
    if all(code in FRAGMENT_CODES for code, _ in errs):
        return "fragment"
    if any(h in msg for _, msg in errs for h in ARTIFACT_HINTS):
        return "artifact"
    return "SUSPECT"


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    per_file = load(pathlib.Path(args[0]))

    if "--emit-baseline" in args:
        for name in sorted(per_file):
            errs = per_file[name]
            if classify(errs) == "SUSPECT":
                for code, msg in sorted({signature(c, m) for c, m in errs}):
                    print(f"{name}: {code}: {msg}")
        return 0

    if "--check-baseline" in args:
        base_path = pathlib.Path(args[args.index("--check-baseline") + 1])
        accepted = set(base_path.read_text().splitlines()) if base_path.exists() else set()
        new: list[str] = []
        for name in sorted(per_file):
            errs = per_file[name]
            if classify(errs) == "SUSPECT":
                for code, msg in sorted({signature(c, m) for c, m in errs}):
                    sig = f"{name}: {code}: {msg}"
                    if sig not in accepted:
                        new.append(sig)
        if new:
            print(f"{len(new)} NEW suspect(s) — fix the rule or review into baseline.txt:")
            for s in new:
                print(f"  - {s}")
            return 1
        n_sus = sum(1 for e in per_file.values() if classify(e) == "SUSPECT")
        print(f"OK: no new suspects ({n_sus} accepted in baseline).")
        return 0

    for name in sorted(per_file):
        errs = per_file[name]
        print(f"== {name} [{classify(errs)}]")
        for code, msg in errs:
            print(f"   TS{code}: {msg}")
    if not per_file:
        print("no errors at all — all Good examples compile clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
