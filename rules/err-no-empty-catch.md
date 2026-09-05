# err-no-empty-catch

> Never silently swallow errors; log, rethrow, or handle

## Why It Matters

Empty `catch {}` turns failures into wrong-but-plausible state: corrupt data, half-written UI, flaky tests that pass. Handling can be minimal (report + fallback), but it must be explicit so the failure is visible.

## Bad

```ts
try {
  await save(data);
} catch {} // save failed — user thinks it worked
```

## Good

```ts
try {
  await save(data);
} catch (e: unknown) {
  report(e);
  showToast("Save failed, retrying with draft kept");
  keepDraft(data);
}
```

## See Also

- [err-unknown-in-catch](err-unknown-in-catch.md) - Narrow before reporting
- [async-try-await](async-try-await.md) - Where the try belongs
