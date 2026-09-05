# checks — verify the skill

Two gates, same as CI:

```bash
bash checks/check.sh   # run from the skill root
```

- `validate.py` — structure, links, index parity. Python only.
- `gen_index.py` — regenerates the marked index regions from `rules/`.
  Check (default) or rewrite with `--write`. Adding a rule means writing the
  rule file, then running `--write`. Never hand-edit inside the markers.
- `gen.py` + `tsc` + `analyze.py` — extracts `## Good` blocks and
  type-checks them. Uses your `tsc` or a cached copy via npx.

`baseline.txt` lists accepted suspects (currently none). The gate fails
only on signatures *not* in it. Regenerate after intentional example
changes and review the diff:

```bash
python3 analyze.py check.log --emit-baseline > baseline.txt
```

Never bless a new entry without reading the rule. Generated files
(`examples/`, `check.log`) are gitignored.
