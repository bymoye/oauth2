<p align="center">
  <img src="docs/assets/nazo-auth-cover.png" alt="Nazo Auth 封面">
</p>

# Nazo Auth Server

[![code-quality](https://github.com/nazozero/NazoAuth/actions/workflows/code-quality.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/code-quality.yml)
[![codeql](https://github.com/nazozero/NazoAuth/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/codeql.yml)
[![dependency-review](https://github.com/nazozero/NazoAuth/actions/workflows/dependency-review.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/dependency-review.yml)
[![conformance-security](https://github.com/nazozero/NazoAuth/actions/workflows/conformance-security.yml/badge.svg?branch=main)](https://github.com/nazozero/NazoAuth/actions/workflows/conformance-security.yml)
[![codecov](https://codecov.io/gh/nazozero/NazoAuth/branch/main/graph/badge.svg)](https://app.codecov.io/gh/nazozero/NazoAuth)

[English](README.md) · [文档](#文档) · [运维](#受支持的部署与运维) · [安全策略](SECURITY.md)

NazoAuth 是用 Rust 编写的自托管 OAuth 2.x / OAuth 2.1-aligned / OpenID
Connect 授权服务器数据面。每个目录管理的租户 issuer 都是同域的：其浏览器 UI、
passkey、CORS、cookie 和协议端点共享该租户的公开 origin。

## 职责与边界

NazoAuth 负责面向 issuer 的协议、本地 identity/admin 管理面、按客户端安全策略、
签名密钥使用和协议状态。PostgreSQL 是用户、client、grant、token、撤销和安全记录的
持久权威来源。Valkey 保存 session、授权码重放标记、PAR、重放检测和限流等短生命周期
协议安全状态。

已发布的安装、更新、备份、恢复和灾难恢复由独立发布的
[`nazoauthctl`](https://github.com/nazozero/NazoAuthCtl) 负责。控制端不是 token
或 authorization 请求的在线依赖。长期运行的 NazoAuth 只拿权限更低的 PostgreSQL
runtime role；生命周期操作通过签名控制端路径使用独立 role。

服务制品不包含 OIDF Suite、浏览器自动化、验证者凭据、计划注册表或验证者专用路由。
外部验证只是普通的公开协议客户端交互；带日期的记录与生产 runtime 分离。详见
[发布边界](docs/operations/release-boundary.zh-CN.md)。

## 当前可核实的支持边界

| 范围 | 已核实边界 |
| --- | --- |
| 包与发布身份 | workspace manifest 是 [Cargo.toml](Cargo.toml)；Release 由已发布的签名 tag 与 attestation 标识，不以本 README 为准。 |
| 运行依赖 | PostgreSQL 是持久权威来源。Valkey 保存短生命周期安全状态，不能作为可独立回滚的普通缓存。 |
| 发布生命周期 | 控制端支持的 install、update、rollback 与 recovery 目标是 Linux `x86_64` 和 `aarch64`；详见[平台支持](docs/operations/platform-support.md)。 |
| TLS 入口 | NazoAuth 支持 `direct-tls` 或受信任反向代理；两种信任模型互斥，详见[部署指南](docs/operations/deployment.zh-CN.md)。 |
| 租户与 issuer 路由 | active directory binding 把规范化请求 Host 映射到一个不可变 tenant graph。未知 Host 没有默认租户回退；Direct TLS 还要求 SNI 与 Host 一致。详见[租户边界](docs/features/tenancy.md)。 |
| 外部登录 federation | 已配置的 external OIDC、OAuth2 social 和受信任 SAML gateway 是可用的产品登录路径。这不同于尚未实现的 OpenID Federation trust-chain protocol；详见[federation](docs/features/federation.md)。 |
| 外部 OIDF 证据 | [official-release 记录](docs/conformance/oidf-2026-09-06-official-release.md)是指定制品的、带日期的工程验收，不是 OIDF 认证声明。 |
| 容量证据 | 性能文档是带日期的测量和回归基线，不承诺当前 Release 的容量。 |

项目实现的 feature 与 profile 以[能力矩阵](docs/protocol/profile-matrix.md)和
[RFC 一致性矩阵](docs/protocol/rfc-compliance-matrix.md)为准。每个 OAuth client
仍必须有显式 grant allowlist、metadata、sender constraint 和当前
`security_policy`；服务端存在某能力不等于 client 已获权。

[路线图](docs/project/roadmap.md)记录尚需前提或独立建模的协议范围。动态 client
注册仍需 initial-access token；external/refresh/ID-token exchange 与 OpenID
Federation trust chain 仍和已实现的租户路由、外部登录 adapter 分开。

## 受支持的部署与运维

已发布的生产安装使用签名控制端生命周期。先从其独立 Release 安装
`nazoauthctl`，注册目标机，并提供已存在且互不相同的 PostgreSQL runtime/lifecycle
role 与 Valkey 凭据：

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

runtime 必须在 `podman`、`docker` 或 `host` 中明确选择一个。NazoAuthCtl 不会
创建或替换 PostgreSQL 与 Valkey 凭据；它为受管操作创建 deployment identity、生成的
应用 secret、签名 identity 和 Valkey state epoch。完整的版本选择、backup、restore-test、
update、rollback 和 recovery 路径见[受管安装、更新与恢复](docs/operations/one-click-update.zh-CN.md)。

通过控制端与公开协议边界运维已安装实例：

```sh
nazoauthctl status --instance production
nazoauthctl doctor --instance production
nazoauthctl operation --instance production --limit 20
```

在目标机私有边界检查 `/health` 和 `/.well-known/openid-configuration`，再经配置的
公开 HTTPS issuer 检查。部署指南给出了启用检查和反向代理/mTLS 边界。

独立二进制可在操作者提供配置、证书、PostgreSQL 与 Valkey 时自己终止 Direct TLS。
没有 `.env.yaml` 时，`nazoauth server` 会创建本地最小配置、生成服务自有 secret 并继续
启动；它不会执行受管 schema 生命周期。`compose.yml` 只是源码树开发沙箱，不是已发布
生产安装路径。

## 配置

配置一个公开 URL，并选择一个传输所有者：

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

不使用反向代理的独立 HTTPS 部署设置 `TRANSPORT_MODE: "direct-tls"`，并按
[配置文档](docs/operations/configuration.md)提供服务端证书、私钥、客户端 CA 和专用
mTLS listener。该文档还定义了 secret 文件输入、持久化 module 状态、state epoch
恢复和授权码重放标记的精确保留语义。

`PUBLIC_BASE_URL` 用于初始化 system tenant 的 directory binding。目录启用后，每个
binding 提供请求 tenant 与 issuer，并由该 issuer 派生该租户的 frontend/CORS 默认值；
cookie 和其他部署级安全设置仍来自进程配置。持久化应用 secret 必须和 PostgreSQL
状态一起备份。Valkey 丢失会中断安全敏感流程；受管数据库恢复会切换
Valkey state epoch，并在重新开放公开入口前完成 token 失效处理。详见
[PostgreSQL 和 Valkey 运维](docs/operations/ha-operations.md)。

## 文档

| 主题 | 链接 |
| --- | --- |
| 文档索引 | [docs/README.md](docs/README.md) |
| 配置与所有权 | [配置](docs/operations/configuration.md) · [清单](docs/operations/configuration-inventory.md) |
| 部署与恢复 | [部署](docs/operations/deployment.zh-CN.md) · [受管生命周期](docs/operations/one-click-update.zh-CN.md) · [HA 运维](docs/operations/ha-operations.md) |
| 标准与 profile | [OpenID Connect](docs/integration/openid-connect.zh-CN.md) · [能力矩阵](docs/protocol/profile-matrix.md) · [RFC 矩阵](docs/protocol/rfc-compliance-matrix.md) |
| 安全与发布 | [威胁模型](docs/security/threat-model.md) · [发布安全](docs/operations/release-security.zh-CN.md) · [SECURITY.md](SECURITY.md) |
| 外部与性能证据 | [一致性记录](docs/conformance/README.md) · [性能索引](docs/performance/README.md) |
| 当前审查记录 | [2026-09-10 项目审查](docs/project/review-2026-09-10.md) |

## 开发

完整测试需要隔离的 PostgreSQL、Valkey、S3 兼容对象存储，以及
[`code-quality.yml`](.github/workflows/code-quality.yml) 中的测试配置与 schema
准备步骤。本地复现应使用该 workflow 的测试环境，不要连接生产数据。

```sh
cargo fmt --check
cargo check --workspace --all-targets --all-features --locked
cargo clippy --workspace --all-targets --all-features --locked -- -D warnings
cargo test --workspace --all-features --locked
```

一次性 Docker HTTP load gate 为：

```sh
python scripts/full_real_request_load.py
```

它在隔离 E2E deployment 中并发检查 health、discovery、client-credentials token
签发和 introspection；它不是性能基准或外部一致性结果。覆盖率运行说明见
[docs/coverage/codecov-docker-runbook.md](docs/coverage/codecov-docker-runbook.md)。

## 许可证

公开源码采用 [AGPL-3.0-or-later](LICENSE)。商业许可只可通过适用著作权人的签署协议
另行授予；详见 [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md)。
