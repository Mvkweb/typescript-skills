# null-exact-optional

> Use `exactOptionalPropertyTypes`; distinguish missing vs explicitly `undefined`

## Why It Matters

Without `exactOptionalPropertyTypes`, `{ a?: string }` accepts `{ a: undefined }`, conflating "not provided" with "provided as undefined". That breaks defaults, spread behavior, and API contracts. Opting in forces callers to omit the key instead of passing `undefined`.

## Bad

```ts
// exactOptionalPropertyTypes: false
type Opts = { title?: string };
const o: Opts = { title: undefined }; // allowed, but was it intentional?
function render(t = "default") { return t; }
render(o.title); // passes undefined explicitly
```

## Good

```ts
// exactOptionalPropertyTypes: true
type Opts = { title?: string };
function render(opts: Opts) {
  const title = opts.title ?? "default"; // handle absence once
  return title;
}
render({}); // ok
// render({ title: undefined }); // error — must omit instead
```

## See Also

- [cfg-strict-true](cfg-strict-true.md) - Related strictness flags
- [type-union-over-sprawl](type-union-over-sprawl.md) - Model absence explicitly
