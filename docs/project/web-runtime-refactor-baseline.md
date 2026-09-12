# Web Runtime Refactor Baseline

## Verification status (2026-09-12)

- Static contracts, 95 Python unit tests, workspace all-target/all-feature check, Actix tests, and transport parity self-test: PASS.
- Clean baseline worktree, `cargo test --locked -p nazo-oauth-server --lib`: PASS (1436 passed, 0 failed, 7 pre-existing ignored; 319.95s). The environment preserves the already committed `RUST_TEST_THREADS=1` from `.github/workflows/code-quality.yml` and supplies isolated PostgreSQL/Valkey. Log: `nazoauth-t00-clean-baseline-test.log` (local validation artifact).
- Diagnostic runs without configured databases failed as expected. Later runs with PostgreSQL/Valkey but without the committed serial test environment also failed (including password worker `Saturated` and several 503 assertions). These runs included new tests and did not prove the clean baseline was broken. No test/runtime timeout, concurrency limit, or production code was changed to make the canonical run pass.
- Thirty-four loaded `framework_boundary_transport` tests: PASS (34 passed, 0 failed, 0 ignored, 3.55s). Explicit `--list` also reports all 34 names. The J3 coverage map below distinguishes real dependencies and observed semantic ports. Artifact: `nazoauth-t00-golden-final.log`.
- DCR audit correction verified: the fake now preserves stored identity like PostgreSQL. PUT retains `client_id`, updates metadata, rotates the registration token, and stale CAS rejects without overwriting the concurrent state. Both corrected tests passed. The previous claim that production PUT rotates `client_id` was caused by the fake and has been withdrawn.
- Official OIDF conformance in both directTLS/RFC9440 variants and comparable load baseline: PENDING — no selected official plan/variant/config/credentials, or running comparable deployment with load dataset and signing identities. Local TLS and RFC9440/CA regression tests passed; those do not constitute official certification or performance evidence.
- Locally present official suite checkout: `oidf-conformance-suite/` at `33a724c7d809a6f9db05cbb513ff2a77cbac905e` (2026-06-29 commit). No selected plan, variant, sanitized config, or result ID was found for this baseline; checkout presence is not an execution result.
- T00 required validation: PASS. The clean baseline full suite, current J3 golden suite, explicit test listing, workspace check, Actix tests, Python/static checks and parity self-test passed. Additional combined Windows full-suite attempts were interrupted at an existing remote TLS test before golden execution; that original test passes focused. Supplementary Linux validation remains pending and does not replace Windows evidence.

- Baseline commit: `ff344fc37d36231ac7e648fd24d0bc657643327f`
- Baseline source tree hashes: `crates/authorization-server/src` = `ce80a4d4a0eac110cbb67d3d5cc0dca96ebff97e`; `crates/http-actix/src` = `f6827b025fcba3d93efd11af9841ce468d62291d`. The baseline commit fixes all other tracked source trees.
- Base commit date in task package: `2026-09-12`
- Working tree observed at task start: dirty (untracked helper scripts in `scripts/`)
- Task baseline assumption: baseline is behaviorally usable; no production behavior edits in this task.

## Baseline manifest hashes

| path | sha256 |
|---|---|
| `Cargo.toml` | `9a462c55fcf05d157c84a6bd653c86217c1a5cdb94d5552416ff4d96371dfd25` |
| `Cargo.lock` | `65eafff759097aff422d7bbf03f8ceaf58baa8df8f1d862dcaee630a81224c98` |
| `.github/workflows/code-quality.yml` | `096af8b4f589843c77bbbb170f773d4ec6fd2274aa5258c54715bdb668a94b63` |
| `.github/workflows/codecov.yml` | `c3412a4c416c5a486247198f198f6007a3ee4f713a7862284736f703efde095c` |
| `.github/workflows/codeql.yml` | `cedcf4d58c428af38d859a5de478296e846b392cb36d3efe279ef6c6cba140f0` |
| `.github/workflows/conformance-security.yml` | `647daf4014c311068d8d6c7e8bae3765c21a583bafb4426b7b486975c8afacbb` |
| `.github/workflows/dependency-review.yml` | `8142bd9c6c1d17353bea838770ec84a68ae81d4584ba010d4d04f942d8336bf3` |
| `.github/workflows/perf-images.yml` | `9cf6bae82c9d0dbcc01847824b1f8ffbc344e61d58c8ec51651afd836ff0b14a` |
| `.github/workflows/release-policy.yml` | `85cf419eddc8c91bd89b8a9c5a94f0797ad972a0d551cea6f850ce7b0f6d80f1` |
| `.github/workflows/release-security.yml` | `994ae32d6f47631234582b97f084d68fa673f7fb14049171dcdb7fef034468b6` |
| `.github/workflows/spec-freshness.yml` | `98a0f91e2cd890d0562538d499d0fc61ff841ad4fa2926616cdc12b8edd851d8` |
| `crates/authorization-server/Cargo.toml` | `007ed75d465c12411aa3c2bebb4c4e5242421c1eb6a2e0a8890d2c71b60f0719` |
| `crates/authorization-server-core/Cargo.toml` | `bb0d1b2b872282af32a9ba8d69b70be08ce97810f4ac0cb1f1383b65f29e269f` |
| `crates/authorization-server-object-store/Cargo.toml` | `378ce120989950b6be56f69133de5a6cb1a2c85fc5613d5c278e1ed9f28ea8a0` |
| `crates/authorization-server-postgres/Cargo.toml` | `eca3dc84e4212d887c4617d8c32d76669f4eeb0d4fd0d08450687612705ecaee` |
| `crates/authorization-server-valkey/Cargo.toml` | `2236e5f71d304c629157cc3a5d655a200015c2a1376a01093d6743d2d44a3d73` |
| `crates/digital-credentials/Cargo.toml` | `907acc40ab465aae15050cbda682c003c73f119962dd23488833acf7353a376d` |
| `crates/http-actix/Cargo.toml` | `6690f8f2129e0263b119cd799daefd72b9ee44e912510e3b337180681e20f99e` |
| `crates/http-signatures/Cargo.toml` | `90befd752561b2dcf0d41e5db87bcdcf664dfed37d4885519dc11812dd2335c0` |
| `crates/identity/Cargo.toml` | `d24d29d2b07edfe29f44f556db05f58e96278e62ec98d8a41bfb0d984d66231f` |
| `crates/key-management/Cargo.toml` | `d65ace789eb607e033c08e668a27769efaeda46d7121c23ee937121bd8a3958c` |
| `crates/nazoauth/Cargo.toml` | `cbc75791f027669d1cd40bba9afd059600bbce68cd3dcb5d37ca73f8eb30a0a1` |
| `crates/openid4vc-http-actix/Cargo.toml` | `20baf7ccdad6448e8fc702383965eb8fa344c21d577a1ce56b3844d861b0e496` |
| `crates/openid4vci/Cargo.toml` | `351aabfe8ff2c1e75662b51c06d6b5b63ddef21a16ddc0ac4b06a82baffea9fe` |
| `crates/openid4vp/Cargo.toml` | `4b0edbae70d76e2a4c43d39e2cd529347bc47b14f516c00ef0e27ef245397ff9` |
| `crates/operator-protocol/Cargo.toml` | `1a2d3c7c0adac1af6a55f40120d1a47484896e629303aba0ccdcf480df95c321` |
| `crates/persistence/Cargo.toml` | `54343accad1a5c1d0ca77d000247eae6346082c846b32d3f8398fcea957a7f3d` |
| `crates/persistence-postgres/Cargo.toml` | `efd1c3651981175425a6fb6bc0c3848e15d5a4ccc859c6a36ea36a3ee55f871d` |
| `crates/resource-server/Cargo.toml` | `53159997b4a7c8f17aa0f877f941de3f67aa8eb2795fdcc3c0e4f0ab46be671e` |
| `crates/runtime-capabilities/Cargo.toml` | `7b7f2296e144793de844247c92a776ee923ded55fb02efc018aa8caf4fe049da` |
| `crates/scim-events/Cargo.toml` | `794ba51ff8e87b0a660c508f81e379de88ad9fa05d56f3a5cae188447a1f1959` |
| `crates/state-store-valkey/Cargo.toml` | `e2c505fb52060d55cab58aed15f99735c1024e5a3293b6c2faef59a98a40bb3c` |
| `fuzz/Cargo.toml` | `10e094af7ed161915f42396d7225486e682eefe3c535b98f1948258446d5a883` |
| `fuzz/Cargo.lock` | `ff0eeaa703dfd9c741ac70313557a62af7792830aac7371da45f7ebe324a9d80` |

## Working tree baseline notes

- Repository had pre-existing untracked scripts not related to this task at task start:
  - `scripts/check_pg.sh`
  - `scripts/fix_pg.sh`
  - `scripts/fix_user.sql`
  - `scripts/fix_user2.sql`
  - `scripts/grant_all.sql`
  - `scripts/grant_runtime.sql`
  - `scripts/restore_prod.sql`
  - `scripts/restore_prod_user.sql`



## J3 golden coverage

All entries are in `crates/authorization-server/tests/unit/http/framework_boundary_transport.rs`; existing tests elsewhere are additional regression coverage, not substitutes for these new cases.

| Boundary | New evidence |
|---|---|
| Rate limiting / malformed body | Exact 429/503 bytes and limiter calls; real PAR duplicate-body rejection plus Valkey counter/TTL |
| Authentication source / certificate priority | Header-body token conflict with malformed certificate stops before operations; real invalid JWT precedes certificate processing, bound JWT fails certificate before subject/client queries |
| DPoP | Duplicate exact error; unbound Bearer ignores malformed and whitespace-only proofs without DPoP state calls; real signed nonce/replay/ath/htu with observed state order |
| mTLS | Real Rustls + Actix peer-certificate capture; forged headers cannot replace connection identity; trusted/untrusted RFC9440; same certificate facts and service observe PostgreSQL tenant CA add/revoke |
| DCR | Stateful store mirrors PostgreSQL identity and CAS semantics; PUT metadata/token rotation, old token rejection on original path, stale CAS preserves concurrent state |
| PAR / JAR | Real PostgreSQL/Valkey PAR keeps repeated resources and ignores unknown extensions, exact URI response and storage fields/TTL; invalid/unsigned/tampered JAR never selects attacker callback |
| JARM / form_post | Real signature/JWKS validation of every JARM claim; exact HTML and headers with nonce cryptographically random and bound to CSP/script |
| CIBA / Device | Real pending/slow_down/denied/approved/replay; issued JWT signatures/claims/mTLS binding; Device invalid CSRF/session leaves state intact, valid denial consumes it; both clearing cookies observed |
| Persisted issuance | Actual PostgreSQL durable response bytes equal first and replay bodies; initial Pragma present, replay absent; issued JWT signatures/claims/binding checked |
| FAPI | Real Ed25519 request and response signatures, exact success/error bytes/challenges, authorization/replay/lookup failure call order, Content-Digest/original digest/interaction-id binding; JSON-equivalent changed request bytes rejected before authorization; signer unavailable returns empty 503 |

Random UUIDs, tokens, signatures, nonces and timestamps remain observable and are validated or rebound in comparisons. They are not stripped from payloads. Local directTLS uses a test Rustls listener with production certificate capture; it does not certify a deployed Native listener or external OIDF plan. CA revocation is verified at the real client-authentication service using the same captured facts, not across a persistent TLS connection.