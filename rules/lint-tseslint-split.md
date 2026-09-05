# lint-tseslint-split

> Pin lint to TS 6 programmatic API until 7.1; type-check with TS 7 `tsc`

## Why It Matters

`typescript-eslint` (and everything built on it) imports the TS programmatic API, which TS 7.0 doesn't ship in stable form — support tops out below 6.1 and the GA-day support request was closed as not-planned. Forcing TS 7 under eslint crashes (`Cannot read properties of undefined`); the supported split is `tsc` 7 for speed, eslint on 6.x until the new 7.1 API lands (~Oct 2026).

## Bad

```jsonc
// eslint crashes: typescript-eslint outside its supported range
{ "devDependencies": { "typescript": "^7.0.0" } }
```

## Good

```jsonc
{
  "devDependencies": {
    "typescript": "npm:@typescript/typescript6@^6.0.2",
    "@typescript/native": "npm:typescript@^7.0.2"
  }
}
```

```bash
npx --package=@typescript/native tsc --noEmit # fast check on 7
npx eslint .                                  # lint on 6 API
```

## See Also

- [cfg-ts7-side-by-side](cfg-ts7-side-by-side.md) - Full side-by-side setup
- [async-no-floating-promises](async-no-floating-promises.md) - Example rule to keep enforcing via eslint
