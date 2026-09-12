# T07 — Token结果闭包与共享签发语义

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T07-FILE-MAP.md`
- `../references/tasks/T07-INTERFACES.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T04.md`
- `../feedback/T06.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T07` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T07.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

让所有token终端分支返回中立结果，删除为Actix response服务的Send补救包装。

## 2. 前置条件

P4纯crypto/config/audit/snapshot；P6客户端认证与facts；整个token返回链在同一闭合Step改签名。

## 3. 精确修改范围

App新增contracts/token_endpoint.rs并完成oauth_error.rs；Native http/token/issue.rs、issue_grant.rs、issue/{authorization_code_state,refresh_persistence}.rs的业务迁App token同名；共享native_sso状态helper迁App token/native_sso.rs。所有grant终端返回点、Native http/token/ciba/poll.rs、http-actix/src/presenter.rs修改；原token unit tests按业务/HTTP拆。

## 4. Symbol 级修改方案

F3为唯一TokenEndpointSuccess/OAuthEndpointError。issue_token_response及各终端grant→Result<TokenEndpointSuccess,OAuthEndpointError>；原TokenIssue/内部状态结果仍按原语义，不把全部内部helper都HTTP化。TokenIssuanceContext/Data/Settings/proxy改Arc+纯config+F2facts，保留pinned key lease。Replayed直接原bytes，Issued仅新响应JSON；PreAuthorized直接VC Operation结果。删除SendCibaResponse、物化/重建response及对应unsafe/Send补救；CibaTokenContext.request改&TokenRequestFacts。OAuthJsonErrorFields仍有authorization消费者，留到P9原子删，不复制新实现。

## 5. 数据流变化

之前：grant → issue helpers → HttpResponse → CIBA send wrapper → HttpResponse。
之后：grant/issue helpers → typed token result → Adapter一次present；CIBA回调自然持有Send-safe事实/结果。

## 6. 必须保持的行为不变量

签发claims、alg/kid/keylease、access/refresh持久化、authorization-code失败标记、refresh-family状态、replay revocation、native SSO binding、DPoP nonce全保持。特别是persisted token成功回放的原始字节不重序列化；Issued/Replayed/PreAuthorized的pragma/nonce差异保持。成功token不因呈现迁移多签一次或多查store。

## 7. 禁止实现方式

不得GenericResponse；不得把全部body降为Value；不得反序列化回放bytes；不得新SendHttpResponse/unsafe Send；不得改变CIBA closure的Send约束；不得凭错误字符串判断业务分支。

## 8. 严格实施步骤

Step 1（原子返回闭包）：落F3结果/error和Adapter映射，同时改所有token终端返回类型，消除HttpResponse在回调中的流动。Step 2：迁issue/issue_grant与两个issue子模块。Step 3：迁native SSO共享状态helper，所有剩余调用明确import唯一App文件。Step 4：拆业务/HTTP测试，删除SendCibaResponse及无消费者helper，检查错误映射与字节快照。

## 9. 每一步局部验证

```bash
# Step 1
cargo check --locked -p nazo-oauth-server -p nazo-http-actix -p nazoauth --all-targets
cargo test --locked -p nazo-http-actix --test presenter_contract
# Steps 2/3
cargo test --locked -p nazo-oauth-server --lib
cargo test --locked -p nazoauth --lib
# Step 4新增App tests/token_outcome.rs
cargo test --locked -p nazo-oauth-server --test token_outcome
cargo test --locked -p nazoauth --lib framework_boundary_transport
python scripts/verify_static_contracts.py --check
rg -n 'SendCibaResponse|unsafe impl Send.*Response' crates
rg -n 'HttpRequest|HttpResponse|actix_' crates/authorization-server/src/token
```

## 10. 任务最终验收标准

三个成功变体有独立golden；所有token业务返回neutral；SendCibaResponse定义/引用为0；code/refresh原子性测试与CIBA回调编译通过；回放原bytes一致。

## 11. 失败处理

先查终端return是否漏改、body是否被序列化两次、CIBA借用是否仍抓住HttpRequest、隐式clone是否改generation。不得重新引入wrapper。签名闭包失败回退Step1整体而非逐grant加转换兼容层。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T07.md`。反馈是后续任务唯一需要读取的历史执行摘要。
