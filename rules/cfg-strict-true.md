# cfg-strict-true

> `strict: true` (default in TS 7); fix code, don't disable flags

## Why It Matters

`strict` bundles `strictNullChecks`, `noImplicitAny`, `useUnknownInCatchVariables`, and more — the flags that make every other rule enforceable. TS 7 defaults it on. Turning off one sub-flag to silence an error trades a local complaint for global unsoundness; fixing the code is almost always cheaper than the bugs loose mode admits.

## Bad

```jsonc
// tsconfig.json — do not do this to "fix" errors
{ "compilerOptions": { "strict": false, "strictNullChecks": false } }
```

## Good

```jsonc
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  }
}
```

Strict mode pays off in ordinary code — this compiles with no assertions:

```ts
function greet(name: string | null): string {
  if (name === null) return "stranger";
  return name.toUpperCase(); // narrowed to string
}
```

## See Also

- [null-strict-null](null-strict-null.md) - The highest-value sub-flag
- [coll-nouncheckedindexedaccess](coll-nouncheckedindexedaccess.md) - Strictness beyond strict
