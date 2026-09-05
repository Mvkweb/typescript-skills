# cfg-verbatim-module-syntax

> Enable `verbatimModuleSyntax`; be explicit about type-only imports

## Why It Matters

Without it, `tsc` silently drops unused value-looking imports, hiding whether `import { X }` was runtime or type. With it on, type-only imports must say `import type`, so emit is predictable, strip-types runners agree with `tsc`, and accidental runtime dependencies on types error out.

## Bad

```jsonc
{ "compilerOptions": { "verbatimModuleSyntax": false } }
```

```ts
import { Config } from "./cfg"; // type or value? bundler must guess
```

## Good

```jsonc
{ "compilerOptions": { "verbatimModuleSyntax": true } }
```

```ts
import type { Config } from "./cfg";
import { loadConfig } from "./cfg";
```

## See Also

- [mod-import-type](mod-import-type.md) - The import discipline
- [cfg-erasable-syntax-only](cfg-erasable-syntax-only.md) - Companion modern flag
