# T06 — UserInfo / FAPI / SCIM / mTLS / 客户端认证

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T06-FILE-MAP.md`
- `../references/tasks/T06-INTERFACES.md`
- `../references/CARGO-DEPENDENCY-PLAN.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T02.md`
- `../feedback/T04.md`
- `../feedback/T05.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T06` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T06.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

消除Framework request穿透安全契约，分开连接提取与协议安全判断。

## 2. 前置条件

T02/T04/T05；FAPI replay Port、SessionResolver、纯crypto与resolver就绪；UserInfo/SCIM定义+签名+实现+调用方同Step迁。

## 3. 精确修改范围

修改http-actix/src/{userinfo,scim,fapi_resource,token_client_auth,token_management,lib}.rs；新增mtls.rs。App contracts/{userinfo,scim}.rs完成；Native domain/{userinfo,resource_server,scim,token_management}.rs迁App；http/mtls拆App security/mtls.rs+Native提取；http/token/client_auth迁App token/client_auth.rs；Native ScimBootstrapPasswordProvider移adapters/security.rs；启动factory与token facts调用更新。

## 4. Symbol 级修改方案

UserInfo按F7两段，PreparedUserinfo外层不可造，不重复decode/revocation；SCIM按F2三facts。FapiResourceAuthorizer与HttpMessageSignatures原neutral签名不改，ServerFapiResourceAuthorizer/MessageSignatures迁App，ServerFapiMtlsResolver改名Native extractor。MtlsClientCertificate重复模型合并到唯一ClientCertificateFacts；client_mtls_certificate_matches及纯chain/DN/SAN/租户策略App，socket/rustls downcast/extensions/RFC9440/trusted-peer判定Native。ClientAuthRequestFacts保留endpoint_path+Option<ClientCertificateFacts>，现有ClientAuthConfig/TokenManagementClientAuthError原样迁。

## 5. 数据流变化

之前：UserInfo/SCIM接HttpRequest；认证读Native certificate；FAPI提取/验证混合。
之后：Actix严格提取专用facts → App；UserInfo prepare → 按需Native mTLS → App binding；FAPI capture → 原neutral request/context → App授权/签名 → HTTP呈现。

## 6. 必须保持的行为不变量

DER leaf/chain顺序、SHA256 base64url thumbprint、DN规范化、SAN排序去重、expiry、公钥校验不变。RFC9440只信任直接socketpeer CIDR，不以XFF/Forwarded建立信任；只请求级缓存提取成功/失败，不跨请求缓存租户CA决策。部署CA/租户CA、自签x5c pin、PKI单identity selector及额外thumbprint收紧保持。UserInfo非法token先于证书错误、未绑定Bearer忽略非必要DPoP，scheme/binding各分支不合并。FAPI原始body/digest/签名失败503/失败响应签名、owned Arc<KeySnapshot>+ptr_eq缓存generation保持。SCIM scope/tenant/replay/cursor/longpoll及introspection/revocation错误/挑战保持。

## 7. 禁止实现方式

不得传HeaderMap整包；不得Host/Forwarded生成DPoP htu；不得所有UserInfo都提前解析证书；不得Any/extensions入App；不得自动把认证证书当token binding；不得跨请求缓存tenantCA；不得只签成功响应。

## 8. 严格实施步骤

Step 1：纯mTLS consumer/ClientAuthRequestFacts迁移及全部Native构造点。Step 2（UserInfo原子）：contracts+两段实现+extractor注入+endpoint/testfake。Step 3：FAPI实现/快照与签名缓存迁App，capture留Adapter。Step 4：SCIM授权/cursor/event signer迁App，hasher/longpoll留外。Step 5：token management迁App共享client-auth，删重复certificate/旧request接口。

## 9. 每一步局部验证

```bash
# Step 1
cargo check --locked -p nazo-oauth-server -p nazo-http-actix -p nazoauth
cargo test --locked -p nazo-key-management --test mtls_trust
cargo test --locked -p nazo-http-actix --test token_client_auth_transport
# Steps 2/3；新增App tests/security_facts.rs
cargo test --locked -p nazo-oauth-server --test security_facts
cargo test --locked -p nazoauth --lib framework_boundary_transport
cargo test --locked -p nazo-resource-server -p nazo-http-signatures
# Step 4
cargo test --locked -p nazo-http-actix --test scim_transport
python scripts/rfc9967_scim_set_e2e.py --source-policy-check
# Step 5
cargo test --locked -p nazo-http-actix
python scripts/verify_static_contracts.py --check
rg -n 'HttpRequest|HttpResponse|actix_|rustls::ServerConnection|extensions\(' crates/authorization-server/src
```

## 10. 任务最终验收标准

UserInfo/SCIM trait无request；certificate model唯一；App无连接extensions；FAPI原neutral模型未重复；golden同值、证书提取/撤销/store/keycache调用次数不增加。

## 11. 失败处理

先查trim/重复header、http版本转换、证书提取顺序、proof_present与proof区别。任意安全回归停止当前Step；不得放宽证书/nonce/message-signature以通过；回退闭合能力，不恢复HttpRequest。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T06.md`。反馈是后续任务唯一需要读取的历史执行摘要。
