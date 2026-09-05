# err-unknown-in-catch

> Catch clause variables are `unknown` under `useUnknownInCatchVariables`; narrow them

## Why It Matters

Anything can be thrown (`throw "oops"`), so `catch (e)` is unsound as `Error`. `useUnknownInCatchVariables` (on under `strict`) forces a check. Narrowing once at the catch site keeps error paths honest without sprinkling `as Error` lies.

## Bad

```ts
try {
  run();
} catch (e) {
  console.log(e.message); // error under strict — e is unknown (good!)
}
```

## Good

```ts
try {
  run();
} catch (e: unknown) {
  if (e instanceof Error) console.log(e.message);
  else console.log("unknown failure", e);
}
```

## See Also

- [err-error-only-throw](err-error-only-throw.md) - Throw Errors so catches work
- [any-unknown-over-any](any-unknown-over-any.md) - Same unknown discipline
