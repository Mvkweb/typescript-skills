# anti-non-null-abuse

> Don't use `!` on values you haven't validated

## Why It Matters

`value!` asserts non-null with no runtime effect — if the refactor that guaranteed presence moves, the crash moves with it silently. The `!` also spreads: readers assume safety and skip checks downstream.

## Bad

```ts
function send(u: { email?: string }) {
  mailer.send(u.email!); // crashes when email missing
}
```

## Good

```ts
function send(u: { email?: string }) {
  if (u.email === undefined) throw new Error("email required");
  mailer.send(u.email);
}
```

## See Also

- [null-no-non-null-assertion](null-no-non-null-assertion.md) - The rule
- [narrow-assertion-fn](narrow-assertion-fn.md) - Validate once, narrow everywhere
