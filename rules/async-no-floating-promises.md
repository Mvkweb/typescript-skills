# async-no-floating-promises

> Never float promises; `await`, `return`, or `void` with handling

## Why It Matters

An un-awaited, un-returned promise detaches errors: rejections become `unhandledrejection` instead of local `try/catch`, and ordering becomes accidental. Marking intent (`await` for sequence, `return` to propagate, `void` + `.catch` for fire-and-forget) keeps failures local.

## Bad

```ts
function onClick() {
  save(data); // floated — errors unhandled, caller can't await
}
```

## Good

```ts
async function onClick() {
  await save(data); // sequenced + catchable
}
function onClickFireAndForget() {
  void save(data).catch(report); // explicit fire-and-forget
}
```

## See Also

- [async-try-await](async-try-await.md) - Catching async errors
- [lint-tseslint-split](lint-tseslint-split.md) - Enforce `@typescript-eslint/no-floating-promises`
