# mod-import-type

> Use `import type` / `export type` with `verbatimModuleSyntax`

## Why It Matters

Without explicit type-only imports, bundlers must guess whether `import { X }` has runtime meaning; a missed guess leaves a runtime import of a type that doesn't exist after stripping. `import type` makes erasure explicit, survives `verbatimModuleSyntax`, and lets bundlers drop the import safely.

## Bad

```ts
import { User, loadUser } from "./user"; // is User runtime or type?
```

## Good

```ts
import { loadUser } from "./user";
import type { User } from "./user";
export type { User };
```

## See Also

- [cfg-verbatim-module-syntax](cfg-verbatim-module-syntax.md) - Enforce it
- [mod-export-types](mod-export-types.md) - Export the types consumers need
