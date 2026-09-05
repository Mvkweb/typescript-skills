# cfg-erasable-syntax-only

> Enable `erasableSyntaxOnly` to stay compatible with native strip-types runtimes

## Why It Matters

Node 22.18+, Deno, and Bun run `.ts` by stripping types without checking. Non-erasable constructs (enums, namespaces, parameter properties) abort stripping or behave differently than `tsc` emit. The flag (TS 5.8+, expected default direction in TS 7 era) turns those into errors at author time instead of runtime surprises.

## Bad

```ts
// erasableSyntaxOnly: false — compiles but won't strip-run
enum E { A }
class C { constructor(private x = 1) {} }
```

## Good

```jsonc
{ "compilerOptions": { "erasableSyntaxOnly": true } }
```

```ts
type E = "A";
class C { x = 1; constructor(x = 1) { this.x = x; } }
```

## See Also

- [enum-erasable-only](enum-erasable-only.md) - What to write instead
- [cfg-bundler-resolution](cfg-bundler-resolution.md) - Modern module setup that pairs with it
