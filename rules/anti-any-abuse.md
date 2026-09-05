# anti-any-abuse

> Don't use `any` to silence the checker

## Why It Matters

`as any` / `: any` converts a compile error into a runtime bug somewhere else, usually far from the cast. Every `any` is tech debt with interest: it disables checking for all downstream uses and hides the real fix (narrowing, branding, or correcting the type).

## Bad

```ts
const user = JSON.parse(raw) as any;
sendEmail(user.emal); // typo — no error, crashes at runtime
```

## Good

```ts
const raw = '{"id":"1","name":"Ada","email":"a@x.io"}';
const user: unknown = JSON.parse(raw);
assertUser(user); // throws on bad shape
sendEmail(user.email); // narrowed — no crash, no cast

function assertUser(v: unknown): asserts v is { id: string; name: string; email: string } {
  if (typeof v !== "object" || v === null) throw new Error("bad user");
  const r = v as Record<string, unknown>;
  if (typeof r.id !== "string" || typeof r.name !== "string" || typeof r.email !== "string") {
    throw new Error("bad user fields");
  }
}
```

## See Also

- [any-no-explicit-any](any-no-explicit-any.md) - The rule
- [anti-assertion-abuse](anti-assertion-abuse.md) - `as` lies are the same debt
