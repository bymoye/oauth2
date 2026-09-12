# T08 — Token各Grant与Dispatcher迁入Application

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T08-FILE-MAP.md`
- `../references/tasks/T08-INTERFACES.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T06.md`
- `../feedback/T07.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T08` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T08.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

移除token用例对HTTP request、具体resolver和其他HTTP endpoint的依赖。

## 2. 前置条件

P7中立返回闭包完成，T06 client-auth与F2facts就绪；不能边迁grant边临时恢复response。

## 3. 精确修改范围

迁Native http/token/{client_credentials,authorization_code,refresh,jwt_bearer,token_exchange,native_sso,device_issuance}.rs，ciba/{poll,policy,state}.rs的token业务至App token。拆dispatch/{mod,client_auth,errors,pre_authorized,rate_limit}.rs；Native http/token.rs留路由/提取/呈现，App token/mod.rs管理子模块。NativeCIBA创建/决定暂留P10，state中的纯业务定义归App。

## 4. Symbol 级修改方案

将ServerTokenService、TokenEndpointHandles/TokenCoreHandles/Openid4vcTokenHandles归App；Data→Arc、具体registry→SnapshotStore、resolver→既有Port、VC Endpoint→CredentialIssuerOperations。prepare_token_request只作原纯前置检查，Adapter限流/parse后调用prepare，再提取certificate与facts，再execute。auth/DPoP/idempotency/header分支按F2-F3保留；credential_issuer不通过HTTP再进入业务。每个原grant函数body整体迁移，只将读取req的地方换其实际所需fact。

## 5. 数据流变化

之前：HTTP token handler → 同目录dispatcher读request → grant → HTTP VC endpoint/response。
之后：HTTP limiter/parse → App prepare → Native证书提取/Facts → App execute/dispatcher/grant → App/VC服务 → typed outcome → presenter。

## 6. 必须保持的行为不变量

grant支持/能力admission/客户端认证方法/PKCE/redirect URI/refresh轮换/授权详情/资源audience/holder binding/断言一次consume不变。普通grant的strict client-attestation pair与preauthorized的first-header语义不同，保留差异。普通DPoP path与preauthorized含query URI不同。idempotency原第一header、trim/长度/hash只做一次；无新数据库写/读/签名。

## 7. 禁止实现方式

不得把事实字段扩展成所有headers；不得新万能TokenRequestContext包含request闭包；不得提前解析证书到限流前；不得统一不同grant的错误优先级；不得重构grant状态机。

## 8. 严格实施步骤

Step 1：client_credentials/code/refresh分别闭合迁入，每个完成编译/原测试。Step 2：jwt_bearer/token_exchange/native_sso分别迁。Step 3：device token issuance/CIBA poll迁，保持state owner唯一。Step 4：dispatcher及preauth迁；Host handler固定F3时序。Step 5：删除旧业务文件/模块重导出，验完整token矩阵。

## 9. 每一步局部验证

```bash
# Steps 1/2每个grant闭合后
cargo check --locked -p nazo-oauth-server -p nazoauth --all-targets
cargo test --locked -p nazo-auth
cargo test --locked -p nazo-oauth-server --lib
# Step 3
cargo test --locked -p nazoauth --lib
# Step 4
cargo test --locked -p nazo-http-actix --test token_client_auth_transport
cargo test --locked -p nazo-openid4vc-http-actix --test transport_contract
cargo test --locked -p nazoauth --lib framework_boundary_transport
# Step 5
python scripts/verify_static_contracts.py --check
rg -n 'HttpRequest|HttpResponse|web::Data|nazo_http_actix|nazo_openid4vc_http_actix|ServerRuntimeModuleRegistry|RemoteClientDocumentResolver' crates/authorization-server/src/token
```

## 10. 任务最终验收标准

App token目录无Framework/concreteadapter；Native token文件只边界；各grant原测试存在并实际运行；client assertion/replay/store调用次数与基线一致；VC preauth直接用语义Operation。

## 11. 失败处理

先查prepare与execute是否重做IO、missing-client的holder-binding错误是否移动、preauth是否误用了strict-header/path-only。安全与事务回归立即停止当前grant Step，不用放宽条件或加新补偿写掩盖。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T08.md`。反馈是后续任务唯一需要读取的历史执行摘要。
