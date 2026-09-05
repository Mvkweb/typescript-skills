# any-no-explicit-any

> Ban explicit `any`; use `unknown` + narrowing instead

## Why It Matters

`any` disables checking for a value and everything derived from it. One `any` parameter silences errors at the call site, inside the function, and in every caller that touches the result. `unknown` forces a narrowing step, so unsafe input is validated once at the boundary instead of leaking.

## Bad

```ts
function parseJson(raw: any) {
  return raw.data.items; // no checking at all
}

const ids: number[] = parseJson(req.body); // unsound, no error
```

## Good

```ts
function parseJson(raw: unknown): { items: unknown[] } {
  if (typeof raw !== "object" || raw === null) throw new Error("bad json");
  if (!("data" in raw)) throw new Error("missing data");
  return raw.data as { items: unknown[] };
}
```

## When `any` Is Acceptable

Only as a narrow escape hatch inside a well-typed wrapper (e.g. interop with untyped JS), never in a public signature. Prefer `unknown` first; reach for `any` last.

## See Also

- [any-unknown-over-any](any-unknown-over-any.md) - `unknown` forces validation
- [any-narrowest-scope](any-narrowest-scope.md) - Contain the blast radius
- [anti-any-abuse](anti-any-abuse.md) - Anti-pattern reference
