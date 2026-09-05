# proj-dev-deps-types

> Put `typescript` + `@types/*` in `devDependencies`; set explicit `types: []`, `rootDir`

## Why It Matters

Types are build-time only; shipping them as runtime `dependencies` bloats installs and confuses bundlers. TS 7 defaults `types: []` (no automatic `@types` inclusion) and `rootDir: ./` — implicit globals and stray `src` nesting that used to work now error. Explicit lists make builds reproducible across machines.

## Bad

```jsonc
{
  "dependencies": { "typescript": "^7.0.0", "@types/node": "^22" },
  "compilerOptions": {}
  // types: auto-included (TS ≤6 behavior assumed), rootDir inferred
}
```

## Good

```jsonc
{
  "devDependencies": { "typescript": "^7.0.2", "@types/node": "^24" },
  "compilerOptions": { "types": ["node"], "rootDir": "./src" },
  "include": ["./src"]
}
```

## See Also

- [cfg-strict-true](cfg-strict-true.md) - Full recommended tsconfig in SKILL.md
- [mod-export-types](mod-export-types.md) - Publish types correctly from libs
