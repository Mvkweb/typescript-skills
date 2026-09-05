# cfg-bundler-resolution

> Use `moduleResolution: bundler` (or `nodenext`); don't use `node10`/`classic`/`baseUrl`

## Why It Matters

`node10`/`classic` resolution and `baseUrl` are deprecated and hard errors in TS 7. They resolve differently than Vite/webpack/Bun, so types pass while the bundler fails (or vice versa). `bundler` matches modern tooling; `nodenext` matches Node ESM exactly. `paths` should be relative to the project root.

## Bad

```jsonc
{
  "compilerOptions": {
    "moduleResolution": "node10",
    "baseUrl": "./src",
    "paths": { "@/*": ["./*"] }
  }
}
```

## Good

```jsonc
{
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler",
    "paths": { "@/*": ["./src/*"] }
  }
}
```

Under `bundler`/`nodenext`, write ESM-style imports so types and the
bundler agree:

```ts
import { load } from "./lib.js";
import type { Config } from "./config.js";
```

## See Also

- [cfg-strict-true](cfg-strict-true.md) - Modern defaults bundle
- [proj-dev-deps-types](proj-dev-deps-types.md) - Explicit `types`/`rootDir` for TS 7
