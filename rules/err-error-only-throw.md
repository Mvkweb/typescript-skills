# err-error-only-throw

> Only `throw Error` (or subclass); never throw strings/objects

## Why It Matters

`throw "bad"` loses stack traces and forces every catcher to handle `unknown` shapes. `Error` carries `message`, `cause`, and stack uniformly, works with `instanceof` narrowing, and plays with logging/reporting tools.

## Bad

```ts
if (!id) throw "missing id"; // no stack, catcher gets string
if (!user) throw { code: 404 }; // shape unknown to catcher
```

## Good

```ts
if (!id) throw new Error("missing id");
if (!user) {
  throw Object.assign(new Error("not found"), { code: 404 });
}
```

## See Also

- [err-unknown-in-catch](err-unknown-in-catch.md) - Narrow what you catch
- [err-no-empty-catch](err-no-empty-catch.md) - Don't swallow what you catch
