#!/usr/bin/env python3
"""Extract `## Good` ```ts blocks from rules/*.md into checks/examples/.

Only Good blocks are extracted: Bad blocks are intentional anti-patterns and
must NOT compile cleanly. Each block becomes one module file so rules can't
interfere with each other; ../support/ambient.d.ts covers shared helper names.

Generated files are disposable (gitignored). Usage:
    cd checks && python3 gen.py
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RULES = ROOT / "rules"
CHECKS = ROOT / "checks"
OUT = CHECKS / "examples"


def good_blocks(text: str) -> list[str]:
    """Return ```ts blocks inside the ## Good section only."""
    m = re.search(r"^## Good\s*$", text, re.M)
    if not m:
        return []
    tail = text[m.end():]
    nxt = re.search(r"^## \S", tail, re.M)
    section = tail[: nxt.start()] if nxt else tail
    return re.findall(r"```ts\n(.*?)```", section, re.S)


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copy(CHECKS / "support" / "ambient.d.ts", OUT / "ambient.d.ts")

    total = 0
    for path in sorted(RULES.glob("*.md")):
        for i, block in enumerate(good_blocks(path.read_text())):
            total += 1
            (OUT / f"{path.stem}--{i}.ts").write_text(
                f"// generated from rules/{path.name} ## Good block {i}\n"
                f"export {{}};\n{block.strip()}\n"
            )
    print(f"extracted {total} Good blocks from {len(list(RULES.glob('*.md')))} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
