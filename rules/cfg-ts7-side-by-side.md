# cfg-ts7-side-by-side

> TS 7 has no programmatic API yet; run `tsc` (7) + `tsc6` (6) side-by-side for eslint/volar until 7.1

## Why It Matters

TypeScript 7.0 (Go, 8–12x faster) ships no stable programmatic API — `typescript-eslint`, Vue/Svelte/Astro template checkers, and webpack loaders that import `typescript` cannot run on it until 7.1 (~Oct 2026). Running CLI type-checks on 7 while lint/editors pin 6.x gets the speed without breaking tooling.

## Bad

```jsonc
// Installing only TS 7 and expecting eslint/volar to work
{ "devDependencies": { "typescript": "^7.0.0" } }
```

## Good

```jsonc
{
  "devDependencies": {
    "typescript": "npm:@typescript/typescript6@^6.0.2",
    "@typescript/native": "npm:typescript@^7.0.2"
  },
  "scripts": {
    "typecheck": "npx --package=@typescript/native tsc --noEmit",
    "lint": "eslint ."
  }
}
```

## See Also

- [lint-tseslint-split](lint-tseslint-split.md) - Lint pinning details
- [perf-parallel-flags](perf-parallel-flags.md) - TS 7 scaling flags
