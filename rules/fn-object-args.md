# fn-object-args

> Pass objects, not positionals, so argument order is self-documenting

## Why It Matters

`(uri, 10, 1, 10, 1)` compiles with any two numbers swapped; reviewers can't tell without the signature open. A single options object names every argument at the call site, makes new optional fields non-breaking, and composes with `Pick`/`Omit`. Skip on hot paths (per-frame render, tokenizers, parsers) where the allocation matters.

## Bad

```ts
function openFile(uri: string, startLine: number, startCol: number, endLine: number, endCol: number) {}
openFile(uri, 10, 1, 1, 10); // swapped columns/lines — compiles fine
```

## Good

```ts
type Selection = { startLine: number; startCol: number; endLine: number; endCol: number };
function openFile(args: { uri: string; selection: Selection }) {}
openFile({ uri, selection: { startLine: 10, startCol: 1, endLine: 10, endCol: 1 } });
```

## See Also

- [type-schema-derived](type-schema-derived.md) - Derive option slices with Pick/Omit
- [gen-no-unnecessary-params](gen-no-unnecessary-params.md) - Keep the options type simple too
