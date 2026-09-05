# perf-explicit-return-lib

> Annotate library return types for faster declaration emit

## Why It Matters

For `.d.ts` emit, `tsc` must print the inferred return type at every export boundary; complex inferred object types are expensive to serialize and can balloon declarations. An explicit annotation is both documentation and a shortcut — the emitter prints what you wrote instead of computing and printing the inferred structure.

## Bad

```ts
// library index.ts — inferred 200-line object type must be printed
export function config() {
  return { server: { host: "x", ports: [80, 443], tls: { on: true } } };
}
```

## Good

```ts
export interface Config { server: { host: string; ports: number[]; tls: { on: boolean } } }
export function config(): Config {
  return { server: { host: "x", ports: [80, 443], tls: { on: true } } };
}
```

## See Also

- [fn-return-type-branches](fn-return-type-branches.md) - When annotations pay off
- [mod-export-types](mod-export-types.md) - Export those return types
