<p align="center">
  <img src="docs/assets/nazo-auth-cover.png" alt="Nazo Auth cover">
</p>

# Nazo Auth Server

[![code-quality](https://github.com/nazozero/NazoAuth/actions/workflows/code-quality.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/code-quality.yml)
[![codeql](https://github.com/nazozero/NazoAuth/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/codeql.yml)
[![dependency-review](https://github.com/nazozero/NazoAuth/actions/workflows/dependency-review.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/dependency-review.yml)
[![conformance-security](https://github.com/nazozero/NazoAuth/actions/workflows/conformance-security.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/conformance-security.yml)
[![codecov](https://codecov.io/gh/nazozero/NazoAuth/branch/main/graph/badge.svg)](https://app.codecov.io/gh/nazozero/NazoAuth)

[中文文档](README.zh-CN.md) · [Documentation](#documentation) · [Operations](#supported-deployment-and-operations) · [Security](SECURITY.md)

NazoAuth is a self-hosted OAuth 2.x / OAuth 2.1-aligned and OpenID Connect
authorization-server data plane written in Rust. Each directory-managed tenant
issuer is same-origin: its browser UI, passkeys, CORS, cookies, and protocol
endpoints share that tenant's public origin.

## Responsibilities and boundaries

NazoAuth owns the issuer-facing protocol, local identity and administration
surface, per-client security policy, signing-key use, and protocol state. It
uses PostgreSQL for durable users, clients, grants, tokens, revocation, and
security records. It uses Valkey for transient protocol security state such as
sessions, authorization-code replay markers, PAR, replay detection, and rate
limits.

Released installation, update, backup, restore, and recovery are owned by the
independently released [`nazoauthctl`](https://github.com/nazozero/NazoAuthCtl).
The controller is not an online dependency of token or authorization requests.
NazoAuth's long-running runtime receives only the less-privileged PostgreSQL
role; lifecycle work uses a distinct role through the signed controller path.

The server artifact contains no OIDF Suite, browser automation, validator
credentials, plan registry, or validator-specific route. External validation is
an ordinary public-protocol client interaction; dated records remain separate
from the production runtime. See the [release boundary](docs/operations/release-boundary.md).

## Current support boundary

| Area | Verified boundary |
| --- | --- |
| Package and release identity | The workspace manifest is [Cargo.toml](Cargo.toml); a release is identified by its published signed tag and attestation, not this README. |
| Runtime dependencies | PostgreSQL is durable authority. Valkey stores transient security state and must not be treated as an independently rollbackable cache. |
| Release lifecycle | Linux `x86_64` and `aarch64` are the supported controller installation, update, rollback, and recovery targets. See [platform support](docs/operations/platform-support.md). |
| TLS ingress | NazoAuth supports either `direct-tls` or a trusted reverse proxy. The two trust models are exclusive; see [deployment](docs/operations/deployment.md). |
| Tenant and issuer routing | Active directory bindings map a canonical request host to one immutable tenant graph. Unknown hosts have no default-tenant fallback; direct TLS also requires matching SNI and Host. See [tenancy](docs/features/tenancy.md). |
| External login federation | Configured external OIDC, OAuth2 social, and trusted SAML-gateway providers are active product login paths. This is distinct from the unimplemented OpenID Federation trust-chain protocol; see [federation](docs/features/federation.md). |
| External OIDF evidence | The [official-release record](docs/conformance/oidf-2026-09-06-official-release.md) is dated engineering acceptance for identified artifacts, not an OIDF certification claim. |
| Capacity evidence | The performance documents are dated measurements and regression baselines, not a capacity promise for the current release. |

The project implements the features and profiles recorded in the
[profile matrix](docs/protocol/profile-matrix.md) and
[RFC compliance matrix](docs/protocol/rfc-compliance-matrix.md). Each OAuth
client still needs its explicit grant allowlist, metadata, sender constraint,
and current `security_policy`; server support does not grant a client access.

The [roadmap](docs/project/roadmap.md) records the remaining prerequisite-gated
or separate protocol scope. Dynamic Client Registration still requires its
initial-access token, and external/refresh/ID-token exchange plus OpenID
Federation trust chains remain separate from the implemented tenant routing and
external-login adapters.

## Supported deployment and operations

For a released production installation, use the signed controller lifecycle.
Install `nazoauthctl` from its own Release, register the target, and provide
existing, distinct PostgreSQL runtime and lifecycle roles plus an existing
Valkey credential:

```sh
nazoauthctl host add production-host --ssh production --privilege sudo
nazoauthctl install --host production-host --name production \
  --public-url https://auth.example.com --runtime podman \
  --database-host db.internal --database-port 5432 --database-name oauth \
  --database-runtime-user nazo_runtime \
  --database-runtime-password-file ./database-runtime-password \
  --database-lifecycle-user nazo_lifecycle \
  --database-lifecycle-password-file ./database-lifecycle-password \
  --valkey-host valkey.internal --valkey-port 6379 \
  --valkey-password-file ./valkey-password
nazoauthctl bind --instance production --label operations \
  --output-secret-file ./production-recovery-secret
nazoauthctl admin create --instance production
```

Select exactly one runtime: `podman`, `docker`, or `host`. NazoAuthCtl does not
create or replace PostgreSQL or Valkey credentials. It creates the deployment
identity, generated application secrets, signing identity, and the Valkey state
epoch for managed operations. The complete supported lifecycle, including
version selection, backup, restore-test, update, rollback, and recovery, is in
[managed installation, update, and recovery](docs/operations/one-click-update.md).

Operate the installed instance through its controller and public protocol
boundary:

```sh
nazoauthctl status --instance production
nazoauthctl doctor --instance production
nazoauthctl operation --instance production --limit 20
```

Check `/health` and `/.well-known/openid-configuration` on the target's private
boundary, then through the configured public HTTPS issuer. The deployment guide
lists the activation checks and reverse-proxy/mTLS boundary.

A standalone binary can own Direct TLS when the operator provides its
configuration, certificates, PostgreSQL, and Valkey. `nazoauth server` creates
a local minimal `.env.yaml` when absent, materializes service-owned secrets,
and continues starting. It does not perform managed schema lifecycle work.
`compose.yml` is a source-tree development sandbox, not the released production
lifecycle path.

## Configuration

Configure one public URL and choose one transport owner:

```yaml
BIND: "0.0.0.0:8000"
PUBLIC_BASE_URL: "https://auth.example.com"
TRANSPORT_MODE: "trusted-proxy"
TRUSTED_PROXY_CIDRS: "127.0.0.1/32"
MTLS_CERTIFICATE_SOURCE: "disabled"
DATABASE_URL: "postgresql://nazo_oauth:<password>@postgres:5432/oauth"
VALKEY_URL: "redis://valkey:6379/0"
DATA_DIR: "/var/lib/nazo_oauth"
RUST_LOG: "info"
```

For standalone HTTPS without a reverse proxy, use `TRANSPORT_MODE: "direct-tls"`
and configure the server certificate, private key, client CA, and dedicated
mTLS listener described in [configuration](docs/operations/configuration.md).
The configuration guide also defines secret-file inputs, persisted module
state, state-epoch recovery, and the precise authorization-code replay-marker
retention rule.

`PUBLIC_BASE_URL` seeds the initial system-tenant directory binding. Once the
directory is active, each binding supplies the request tenant and issuer; its
issuer derives that tenant's frontend and CORS defaults. Cookie and other
deployment-wide security settings remain process configuration. Back up durable
application secrets and the PostgreSQL state together. Valkey loss interrupts security-sensitive flows; a managed database
restore changes the Valkey state epoch and applies token invalidation before
public ingress reopens. See [PostgreSQL and Valkey operations](docs/operations/ha-operations.md).

## Documentation

| Topic | Link |
| --- | --- |
| Documentation index | [docs/README.md](docs/README.md) |
| Configuration and ownership | [configuration](docs/operations/configuration.md) · [inventory](docs/operations/configuration-inventory.md) |
| Deployment and recovery | [deployment](docs/operations/deployment.md) · [managed lifecycle](docs/operations/one-click-update.md) · [HA operations](docs/operations/ha-operations.md) |
| Standards and profiles | [OpenID Connect](docs/integration/openid-connect.md) · [profile matrix](docs/protocol/profile-matrix.md) · [RFC matrix](docs/protocol/rfc-compliance-matrix.md) |
| Security and release | [threat model](docs/security/threat-model.md) · [release security](docs/operations/release-security.md) · [SECURITY.md](SECURITY.md) |
| External and performance evidence | [conformance records](docs/conformance/README.md) · [performance index](docs/performance/README.md) |
| Current review record | [2026-09-10 project review](docs/project/review-2026-09-10.md) |

## Development

The full test gate requires isolated PostgreSQL, Valkey, and S3-compatible
object storage, plus the test configuration and schema setup in
[`code-quality.yml`](.github/workflows/code-quality.yml). Use that workflow's
fixtures when reproducing the gate locally; never point it at production data.

```sh
cargo fmt --check
cargo check --workspace --all-targets --all-features --locked
cargo clippy --workspace --all-targets --all-features --locked -- -D warnings
cargo test --workspace --all-features --locked
```

The disposable Docker HTTP load gate is:

```sh
python scripts/full_real_request_load.py
```

It exercises health, discovery, client-credentials token issuance, and
introspection under concurrency against its isolated E2E deployment. It is not
a performance benchmark or external-conformance result. Coverage instructions
are in [docs/coverage/codecov-docker-runbook.md](docs/coverage/codecov-docker-runbook.md).

## License

The public source code is licensed under [AGPL-3.0-or-later](LICENSE). A
separate commercial license may be available only through a signed agreement
with the applicable copyright holders; see
[COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md).
