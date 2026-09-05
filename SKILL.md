---
name: typescript-skills
description: >
  TypeScript coding guidelines. Use when writing, reviewing, or refactoring .ts/.tsx files or tsconfig.
license: MIT
metadata:
  author: Mvk
  version: "0.1.0"
  sources:
    - Effective TypeScript (Dan Vanderkam, O'Reilly 2nd ed)
    - Total TypeScript tips (Matt Pocock)
    - Learning TypeScript (Josh Goldberg)
    - TypeScript Handbook (Microsoft)
    - TypeScript 7.0 GA notes (Daniel Rosenwasser / TS team)
    - typescript-eslint docs
---

# TypeScript Best Practices

Comprehensive guide for writing high-quality, idiomatic TypeScript that stays type-safe at scale. Contains 63 rules across 19 categories, prioritized by impact to guide LLMs in code generation and refactoring. Current for TypeScript 7.0 (Go-native `tsc`, 2026).

TypeScript's job is to catch bugs before runtime while staying out of the way. Out of the box, agents write *decent* TypeScript at best: `any` everywhere, `!` to silence errors, enums and namespaces that break `erasableSyntaxOnly`, sprawling optional properties instead of unions, and missing tsconfig strictness that makes the rest pointless. These rules encode what expert TypeScript looks like.

## When to Apply

Reference these guidelines when:

- Writing new TypeScript functions, types, or modules
- Modeling domain state with unions, brands, or discriminated unions
- Handling `null`/`undefined`, errors, or async code
- Writing generics, conditional types, or type-level helpers
- Designing public APIs for libraries (`.d.ts` emit matters)
- Reviewing code for `any` leaks, unsound assertions, or `!` abuse
- Migrating to TypeScript 7.0 (Go `tsc`, `--checkers`, breaking tsconfig defaults)
- Tuning editor/build performance or fixing slow types
- Refactoring existing TypeScript code

## Rule Categories by Priority

<!-- gen:begin:table -->
| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Any & Unknown Safety | CRITICAL | `any-` | 4 |
| 2 | Null & Undefined Safety | CRITICAL | `null-` | 4 |
| 3 | Narrowing & Type Guards | CRITICAL | `narrow-` | 6 |
| 4 | Type Design & Domain Modeling | HIGH | `type-` | 8 |
| 5 | Generics & Inference | HIGH | `gen-` | 4 |
| 6 | Functions & Signatures | HIGH | `fn-` | 4 |
| 7 | Error Handling | HIGH | `err-` | 3 |
| 8 | Async & Concurrency | HIGH | `async-` | 3 |
| 9 | Objects, Arrays & Collections | MEDIUM | `coll-` | 4 |
| 10 | Enums, Literals & Erasable Syntax | MEDIUM | `enum-` | 2 |
| 11 | Classes & OOP | MEDIUM | `class-` | 2 |
| 12 | Modules & Declarations | MEDIUM | `mod-` | 2 |
| 13 | Config & Compiler (TS 7) | MEDIUM | `cfg-` | 5 |
| 14 | Performance (types + build) | MEDIUM | `perf-` | 2 |
| 15 | Testing (types) | MEDIUM | `test-` | 1 |
| 16 | Documentation (TSDoc) | MEDIUM | `doc-` | 1 |
| 17 | Linting & Tooling | LOW | `lint-` | 1 |
| 18 | Project Structure | LOW | `proj-` | 1 |
| 19 | Anti-patterns | REFERENCE | `anti-` | 6 |
<!-- gen:end:table -->

---

## Quick Reference

<!-- gen:begin:quickref -->
### 1. Any & Unknown Safety (CRITICAL)

- [`any-no-explicit-any`](rules/any-no-explicit-any.md) - Ban explicit `any`; use `unknown` + narrowing instead
- [`any-unknown-over-any`](rules/any-unknown-over-any.md) - Use `unknown` for values with an unknown type
- [`any-evolving-any`](rules/any-evolving-any.md) - Avoid evolving-`any` arrays; annotate accumulator types
- [`any-narrowest-scope`](rules/any-narrowest-scope.md) - Keep `any` (when unavoidable) in the narrowest scope, hide behind typed boundary

### 2. Null & Undefined Safety (CRITICAL)

- [`null-strict-null`](rules/null-strict-null.md) - Enable `strictNullChecks` (on by default in TS 7); never turn it off
- [`null-perimeter`](rules/null-perimeter.md) - Push `null`/`undefined` to the perimeter; don't sprinkle through aliases
- [`null-no-non-null-assertion`](rules/null-no-non-null-assertion.md) - Avoid postfix `!`; narrow instead
- [`null-exact-optional`](rules/null-exact-optional.md) - Use `exactOptionalPropertyTypes`; distinguish missing vs explicitly `undefined`

### 3. Narrowing & Type Guards (CRITICAL)

- [`narrow-discriminated-union`](rules/narrow-discriminated-union.md) - Model state as discriminated unions with literal `kind`, not optional sprawl
- [`narrow-exhaustive-never`](rules/narrow-exhaustive-never.md) - Use `never` in `default` for exhaustiveness checking
- [`narrow-type-predicate`](rules/narrow-type-predicate.md) - Write `x is T` predicates for `filter`/custom guards
- [`narrow-assertion-fn`](rules/narrow-assertion-fn.md) - Use `asserts x is T` functions to validate at boundaries
- [`narrow-in-operator`](rules/narrow-in-operator.md) - Prefer `in` / `typeof` / `instanceof` guards over truthiness for objects
- [`narrow-schema-first`](rules/narrow-schema-first.md) - Use the repo's existing schema library before hand-writing property guards

### 4. Type Design & Domain Modeling (HIGH)

- [`type-sets-mental-model`](rules/type-sets-mental-model.md) - Think of types as sets; `extends` = subset = assignable
- [`type-valid-states`](rules/type-valid-states.md) - Prefer types that only represent valid states
- [`type-union-over-sprawl`](rules/type-union-over-sprawl.md) - Prefer unions of interfaces over interfaces with unions
- [`type-brand-nominal`](rules/type-brand-nominal.md) - Use brands for nominal typing (IDs, units, validated strings)
- [`type-satisfies-conformance`](rules/type-satisfies-conformance.md) - Use `satisfies` to check conformance without widening literals
- [`type-constructive-modeling`](rules/type-constructive-modeling.md) - Build types from parts that are all legal instead of restricting loose types
- [`type-simplest-total`](rules/type-simplest-total.md) - Keep `T[]` while every operation stays total; strengthen only where looseness forces lies
- [`type-schema-derived`](rules/type-schema-derived.md) - Derive from existing schema/generated types via `Pick`/`Omit`/`Parameters`/`ReturnType` before declaring new interfaces

### 5. Generics & Inference (HIGH)

- [`gen-no-unnecessary-params`](rules/gen-no-unnecessary-params.md) - Avoid unnecessary type parameters; use what's there
- [`gen-conditional-over-overload`](rules/gen-conditional-over-overload.md) - Prefer conditional types to overload signatures where possible
- [`gen-keyof-sets`](rules/gen-keyof-sets.md) - Remember `keyof (A & B)` vs `keyof (A | B)` set logic; use `keyof typeof` for objects
- [`gen-extends-constraint`](rules/gen-extends-constraint.md) - Use `extends` to constrain and narrow generics

### 6. Functions & Signatures (HIGH)

- [`fn-return-type-branches`](rules/fn-return-type-branches.md) - Omit return types for simple inference; require them for multi-branch + all library exports
- [`fn-no-inferable-annotation`](rules/fn-no-inferable-annotation.md) - Don't annotate what inference already knows; annotate boundaries
- [`fn-whole-expression`](rules/fn-whole-expression.md) - Apply types to entire function expressions, not just parameters
- [`fn-object-args`](rules/fn-object-args.md) - Pass objects, not positionals, so argument order is self-documenting

### 7. Error Handling (HIGH)

- [`err-unknown-in-catch`](rules/err-unknown-in-catch.md) - Catch clause variables are `unknown` under `useUnknownInCatchVariables`; narrow them
- [`err-error-only-throw`](rules/err-error-only-throw.md) - Only `throw Error` (or subclass); never throw strings/objects
- [`err-no-empty-catch`](rules/err-no-empty-catch.md) - Never silently swallow errors; log, rethrow, or handle

### 8. Async & Concurrency (HIGH)

- [`async-no-floating-promises`](rules/async-no-floating-promises.md) - Never float promises; `await`, `return`, or `void` with handling
- [`async-all-parallel`](rules/async-all-parallel.md) - Use `Promise.all` for independent work, sequential `await` only when dependent
- [`async-try-await`](rules/async-try-await.md) - `await` inside `try` when you intend to catch; return bare promise to propagate

### 9. Objects, Arrays & Collections (MEDIUM)

- [`coll-nouncheckedindexedaccess`](rules/coll-nouncheckedindexedaccess.md) - Enable `noUncheckedIndexedAccess`; index access is `T | undefined`
- [`coll-readonly-collections`](rules/coll-readonly-collections.md) - Prefer `readonly` arrays / `Readonly<T>` for inputs you don't mutate
- [`coll-record-sync`](rules/coll-record-sync.md) - Use `Record` to keep keys/values in sync; avoid bare index signatures
- [`coll-iterate-objects`](rules/coll-iterate-objects.md) - Iterate objects with typed `Object.keys`/`entries` helpers, not untyped `for-in`

### 10. Enums, Literals & Erasable Syntax (MEDIUM)

- [`enum-erasable-only`](rules/enum-erasable-only.md) - Write erasable-only syntax; no runtime enums/namespaces/parameter properties
- [`enum-literal-union`](rules/enum-literal-union.md) - Prefer string literal unions + `as const` objects over `enum`

### 11. Classes & OOP (MEDIUM)

- [`class-private-field`](rules/class-private-field.md) - Prefer `#private` ECMAScript fields over TS `private` for real privacy
- [`class-no-getter-abuse`](rules/class-no-getter-abuse.md) - Don't write Java-style get/set pairs; use plain properties or methods

### 12. Modules & Declarations (MEDIUM)

- [`mod-import-type`](rules/mod-import-type.md) - Use `import type` / `export type` with `verbatimModuleSyntax`
- [`mod-export-types`](rules/mod-export-types.md) - Export every type that appears in a public API signature

### 13. Config & Compiler (TS 7) (MEDIUM)

- [`cfg-strict-true`](rules/cfg-strict-true.md) - `strict: true` (default in TS 7); fix code, don't disable flags
- [`cfg-erasable-syntax-only`](rules/cfg-erasable-syntax-only.md) - Enable `erasableSyntaxOnly` to stay compatible with native strip-types runtimes
- [`cfg-verbatim-module-syntax`](rules/cfg-verbatim-module-syntax.md) - Enable `verbatimModuleSyntax`; be explicit about type-only imports
- [`cfg-bundler-resolution`](rules/cfg-bundler-resolution.md) - Use `moduleResolution: bundler` (or `nodenext`); don't use `node10`/`classic`/`baseUrl`
- [`cfg-ts7-side-by-side`](rules/cfg-ts7-side-by-side.md) - TS 7 has no programmatic API yet; run `tsc` (7) + `tsc6` (6) side-by-side for eslint/volar until 7.1

### 14. Performance (types + build) (MEDIUM)

- [`perf-explicit-return-lib`](rules/perf-explicit-return-lib.md) - Annotate library return types for faster declaration emit
- [`perf-parallel-flags`](rules/perf-parallel-flags.md) - Scale TS 7 with `--checkers`/`--builders`; use `--singleThreaded` only to debug

### 15. Testing (types) (MEDIUM)

- [`test-expect-type`](rules/test-expect-type.md) - Test types with `expectTypeOf` / `assertType`, not just runtime tests

### 16. Documentation (TSDoc) (MEDIUM)

- [`doc-no-repeat-types`](rules/doc-no-repeat-types.md) - Don't repeat type info in docs; document intent, units, and invariants

### 17. Linting & Tooling (LOW)

- [`lint-tseslint-split`](rules/lint-tseslint-split.md) - Pin lint to TS 6 programmatic API until 7.1; type-check with TS 7 `tsc`

### 18. Project Structure (LOW)

- [`proj-dev-deps-types`](rules/proj-dev-deps-types.md) - Put `typescript` + `@types/*` in `devDependencies`; set explicit `types: []`, `rootDir`

### 19. Anti-patterns (REFERENCE)

- [`anti-any-abuse`](rules/anti-any-abuse.md) - Don't use `any` to silence the checker
- [`anti-non-null-abuse`](rules/anti-non-null-abuse.md) - Don't use `!` on values you haven't validated
- [`anti-assertion-abuse`](rules/anti-assertion-abuse.md) - Don't use `as` to lie to the compiler; fix the type
- [`anti-enum-runtime`](rules/anti-enum-runtime.md) - Don't use runtime `enum` when a union would do
- [`anti-optional-sprawl`](rules/anti-optional-sprawl.md) - Don't model exclusive states with piles of optionals
- [`anti-stringly-typed`](rules/anti-stringly-typed.md) - Don't use bare `string` where a literal union, brand, or enum-object fits
<!-- gen:end:quickref -->

---

## Recommended tsconfig.json (TS 7)

```jsonc
{
  "compilerOptions": {
    "strict": true, // default true in TS 7 — keep it
    "target": "es2024", // TS 7 default ≈ current stable minus esnext
    "module": "esnext",
    "moduleResolution": "bundler",
    "erasableSyntaxOnly": true, // no enums/namespaces/parameter properties
    "verbatimModuleSyntax": true, // require import type where appropriate
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noUncheckedSideEffectImports": true,
    "useUnknownInCatchVariables": true, // default under strict
    "declaration": true,
    "sourceMap": true,
    // TS 7 only: tune workers; default checkers=4
    // "checkers": 4 — pass via CLI: tsc --checkers 8
    "types": [], // explicit; add "node", "jest" as needed (TS 7 default [])
    "rootDir": "./src",
    "outDir": "./dist",
    "skipLibCheck": true
  },
  "include": ["./src"]
}
```

TS 7 CLI scaling:

```bash
tsc --checkers 8            # more type-checker workers (default 4)
tsc --builders 4            # parallel project references with --build
tsc --singleThreaded        # debug / constrained CI only
```

Side-by-side until 7.1 (no stable programmatic API in 7.0):

```jsonc
// package.json
{
  "devDependencies": {
    "typescript": "npm:@typescript/typescript6@^6.0.2", // tsc6 for eslint/volar
    "@typescript/native": "npm:typescript@^7.0.2"       // tsc (Go) for type-check
  }
}
```

---

## How to Use

This skill provides rule identifiers for quick reference. When generating or reviewing TypeScript code:

1. **Check relevant category** based on task type
2. **Apply rules** with matching prefix
3. **Prioritize** CRITICAL > HIGH > MEDIUM > LOW
4. **Read rule files** in `rules/` for detailed examples

### Rule Application by Task

| Task | Primary Categories |
|------|-------------------|
| New function | `fn-`, `narrow-`, `null-`, `any-` |
| New type/API | `type-`, `gen-`, `mod-`, `doc-` |
| Generics / utility types | `gen-`, `type-`, `perf-` |
| Async code | `async-`, `err-` |
| Error handling | `err-`, `narrow-` |
| Data fetching / validation | `narrow-`, `type-`, `coll-` |
| Library code / .d.ts | `fn-`, `mod-`, `perf-`, `doc-` |
| tsconfig / migration to TS 7 | `cfg-`, `perf-`, `lint-`, `proj-` |
| Code review | `anti-`, `lint-` |

---

## Sources & Attribution

Independent synthesis of official guidance and human expert sources. Not affiliated with or endorsed by Microsoft or any author; examples are original summaries.

**Books & human experts**

- [Effective TypeScript, 2nd ed (83 Items)](https://effectivetypescript.com) — Dan Vanderkam (ex-Google, Sidewalk Labs)
- [Total TypeScript tips](https://www.totaltypescript.com/tips) — Matt Pocock (ex-Vercel)
- [Learning TypeScript](https://www.learningtypescript.com) — Josh Goldberg (typescript-eslint, Microsoft MVP)
- [TypeScript Handbook: Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html), [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) — Microsoft TS team

**Tooling & release notes**

- [Announcing TypeScript 7.0 (Go native, 8–12x)](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) — Daniel Rosenwasser
- [TSConfig Reference](https://www.typescriptlang.org/tsconfig/) (`erasableSyntaxOnly`, `verbatimModuleSyntax`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`)
- [typescript-eslint](https://typescript-eslint.io) — blocked on TS 7 programmatic API until 7.1; pin to 6.x for lint

MIT-licensed. Upstream materials remain under their own licenses.
