# mod-export-types

> Export every type that appears in a public API signature

## Why It Matters

`export function load(): Config` without exporting `Config` forces consumers into `ReturnType<typeof load>` gymnastics and breaks declaration emit for isolated setups. Exported param/return types make libraries self-describing and let `tsc` emit `.d.ts` without inventing anonymous names.

## Bad

```ts
interface Config { url: string } // not exported
export function load(): Config { return { url: "/" }; }
// Consumer can't name Config — must use ReturnType<typeof load>
```

## Good

```ts
export interface Config { url: string }
export function load(): Config { return { url: "/" }; }
import type { Config } from "./lib"; // usable directly
```

## See Also

- [mod-import-type](mod-import-type.md) - Consume those exports cleanly
- [fn-return-type-branches](fn-return-type-branches.md) - Annotate library returns
