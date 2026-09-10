<div align="center">
  <h1>NazoAuth</h1>
  <p>使用 Rust 构建的 OAuth 2.0 与 OpenID Connect 服务。</p>
  <p>
    <a href="https://github.com/nazozero/NazoAuth/actions/workflows/code-quality.yml"><img src="https://github.com/nazozero/NazoAuth/actions/workflows/code-quality.yml/badge.svg?branch=main" alt="代码质量"></a>
    <a href="https://github.com/nazozero/NazoAuth/releases"><img src="https://img.shields.io/github/v/release/nazozero/NazoAuth?label=release" alt="发布版本"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0--or--later-2563eb" alt="AGPL-3.0-or-later"></a>
  </p>
  <p>
    <a href="docs/operations/one-click-update.zh-CN.md">部署</a> ·
    <a href="docs/integration/openid-connect.zh-CN.md">接入应用</a> ·
    <a href="docs/protocol/rfc-compliance-matrix.md">协议状态</a> ·
    <a href="README.md">English</a>
  </p>
</div>

在自己的基础设施上管理登录、令牌签发和应用授权。NazoAuth 支持通行密钥、MFA、
租户路由和外部身份提供方。PostgreSQL 保存持久化状态；Valkey 保存会话、重放保护和短期协议状态。

> [!WARNING]
> **0.5.0 之前，本项目快速迭代，版本更新不做任何历史兼容。**
> 配置、持久化状态、管理接口和控制消息均以当前格式为准。
> 升级前备份，并按目标版本的要求准备部署；项目不维护旧格式读取、转换或兼容层。

## 能力

| 领域 | 支持内容 |
| --- | --- |
| 应用授权 | Authorization Code + PKCE、客户端凭据、刷新令牌轮换、令牌内省与撤销、设备授权、CIBA poll/ping |
| 请求与令牌保护 | PAR、JAR、JARM、DPoP、mTLS、客户端独立安全策略、FAPI 2.0 控制 |
| 身份认证 | 密码、通行密钥、TOTP MFA、外部 OIDC、QQ/微信适配器、受信 SAML 网关 |
| 多租户 | 按 Host 选择 issuer，隔离服务图、签名密钥、客户端、会话和存储 |
| 身份管理 | 账号资料、客户端与授权管理、SCIM 用户供应、安全事件 |
| 数字凭据 | OpenID4VCI 签发与 OpenID4VP 出示，按部署配置凭据类型及信任材料 |

服务公布某项能力，不等于每个客户端都能使用它。
[能力策略](docs/protocol/composable-capability-policy.md)列出了默认值、启用条件和客户端控制。
Implicit、Hybrid、密码授权、未签名 Request Object 和 CIBA push 不受支持。

## 部署

使用 [NazoAuthCtl](https://github.com/nazozero/NazoAuthCtl) 在本机或 SSH 主机上安装并管理正式版本。
运行方式可选 Docker、Podman 或宿主机二进制。部署前需要准备公网 HTTPS issuer、
具有独立 runtime/lifecycle 角色的 PostgreSQL，以及 Valkey。

<details>
<summary><strong>在 SSH 主机上安装</strong></summary>

先在两端安装 NazoAuthCtl，远端 helper 必须与控制端构建一致。
使用已有的 OpenSSH 别名，并将示例中的 release tag 替换为目标签名版本。

~~~sh
nazoauthctl host add production-host --ssh production --privilege sudo

nazoauthctl install \
  --host production-host --name production \
  --to '<nazoauth-release-tag>' \
  --runtime podman --public-url https://auth.example.com \
  --database-host db.internal --database-port 5432 \
  --database-name nazoauth \
  --database-runtime-user nazo_runtime \
  --database-runtime-password-file ./database-runtime-password \
  --database-lifecycle-user nazo_lifecycle \
  --database-lifecycle-password-file ./database-lifecycle-password \
  --valkey-host valkey.internal --valkey-port 6379 \
  --valkey-password-file ./valkey-password

nazoauthctl admin create --instance production
~~~

登录 https://auth.example.com/ui/auth 并完成 MFA 绑定，再使用该管理员账号绑定控制端：

~~~sh
nazoauthctl bind --instance production --label operations \
  --output-secret-file ./production-recovery-secret
nazoauthctl verify --instance production
~~~

离线保管恢复密钥。创建首个管理员使用目标机的本地部署权限；
控制端绑定则需要该管理员和新的 MFA 授权。

</details>

[安装指南](docs/operations/one-click-update.zh-CN.md)包含完整流程、备份验证、更新和恢复。
[TLS 与部署](docs/operations/deployment.zh-CN.md)说明了反向代理和健康检查。
外部 PostgreSQL、Valkey 由部署方管理。

## 接入应用

从 issuer 的 Discovery 文档开始：

~~~text
https://auth.example.com/.well-known/openid-configuration
~~~

注册客户端及其精确回调地址，使用 Authorization Code 和 S256 PKCE。
[OIDC 接入指南](docs/integration/openid-connect.zh-CN.md)覆盖客户端注册、发现、授权、令牌和退出登录。

每个客户端保存独立的安全策略。按应用需要授权 grant 和令牌保护方式；
启用服务端模块不会向所有客户端开放访问权限。

## 服务结构

一个可执行程序组合协议内核、身份服务和存储适配器。请求进入业务处理前，先完成租户选择。

~~~mermaid
flowchart LR
    Apps["应用与用户"] --> TLS["HTTPS"]
    TLS --> Server["NazoAuth · 按 Host 选择租户"]
    Server --> PG[("PostgreSQL")]
    Server --> VK[("Valkey")]
    Server --> Objects["本地或 S3 头像存储"]
    Ctl["NazoAuthCtl"] --> Host["本机 / SSH 主机"]
    Host --> Server
~~~

PostgreSQL 是租户目录和持久化安全状态的权威来源。
每个活跃租户拥有独立服务图和签名密钥生命周期。
Host 路由读取进程内的不可变索引，未知 Host 会被拒绝。
具体边界见[架构](docs/project/architecture.md)与[租户模型](docs/features/tenancy.md)。

## 开发与验证

使用仓库固定的 Rust 工具链。涉及 PostgreSQL、Valkey 和对象存储的测试，需要准备
[质量工作流](.github/workflows/code-quality.yml)中定义的隔离服务与测试配置。

~~~sh
cargo build --release --locked
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features --locked -- -D warnings
cargo test --workspace --all-features --locked
~~~

[测试说明](docs/project/testing.md)列出了检查项与外部测试环境。
[一致性验证记录](docs/conformance/README.md)注明了每次黑盒验证对应的制品与条件；
这些记录属于工程验证，不代表 OIDF 认证。

## 文档

| 接入与开发 | 部署与运维 |
| --- | --- |
| [OIDC 接入](docs/integration/openid-connect.zh-CN.md) | [配置](docs/operations/configuration.md) |
| [通行密钥](docs/features/passkeys.md) · [MFA](docs/features/mfa.md) | [部署与 TLS](docs/operations/deployment.zh-CN.md) |
| [身份联邦](docs/features/federation.md) | [高可用](docs/operations/ha-operations.md) |
| [SCIM](docs/features/scim.md) | [安全模型](docs/security/threat-model.md) |
| [协议覆盖](docs/protocol/rfc-compliance-matrix.md) | [性能测量](docs/performance/README.md) |

漏洞报告见 [SECURITY.md](SECURITY.md)，贡献规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

项目使用 [AGPL-3.0-or-later](LICENSE) 许可证。[商业许可](COMMERCIAL-LICENSE.md)须另行签署协议。
