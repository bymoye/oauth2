# T09 — Authorization / PAR / JAR / JARM与决策迁移

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T09-FILE-MAP.md`
- `../references/tasks/T09-INTERFACES.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T04.md`
- `../feedback/T05.md`
- `../feedback/T06.md`
- `../feedback/T07.md`
- `../feedback/T08.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T09` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T09.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

协议控制流在Application内完成，HTTP response不再反向承载决定所需信息。

## 2. 前置条件

T04–P8共享模型与typed errors就绪；decision contracts已在App；SessionResolver可用。

## 3. 精确修改范围

迁Native http/authorization/{config,jar,consent,presentation,par,mod}.rs中业务到App authorization；request/{parameters,policy,prompt_none,pushed,reauth,response}.rs整体或业务部分迁App；request/form.rs留Native；request/flow.rs拆App操作与Nativehandler。domain/authorization_decision.rs迁App。Native http/views.rs只append_query纯helper迁App authorization/presentation.rs，其余HTML留Native。http-actix/src/presenter.rs删除OAuthJsonErrorFields。

## 4. Symbol 级修改方案

F8为唯一AuthorizationApplication/typed outcomes。authorize/par/consent/client_presentation均无request/response/Settings。原AuthorizationRequestContext只持语义引用与facts。JAR/PAR consume/authorization_error_redirect读typed error code，presentation最后执行。AuthorizationDecisionOperations实现改App services/session/audit。ClientPresentation错误与consent投影按F8。跨crate改pub仅开放外层实际调用面，内部protected_authorization_response_jwt等不变。

## 5. 数据流变化

之前：authorize → apply JAR → HttpResponse error → extension提取 → 决定redirect。
之后：Native parse/sessionfacts → App authorize/PAR/JAR/security → typed outcome/error → Native/Actix redirect/form_post/JSON。

## 6. 必须保持的行为不变量

client/redirect URI先验证后重定向，PAR/JAR原子消费/replay/JTI/nonce/clockskew/JWE/JARM签名及session状态不变。重复resource、扩展参数剔除和parser顺序不变。authorize302、decision303、PAR201、form_post转义/CSP/header、session_state、CSRF保持。ClientPresentation仅error JSON；consent原所有业务字段加csrf，不统一缓存header。

## 7. 禁止实现方式

不得从HttpResponse读协议error；不得把JARM/redirect安全校验搬Adapter；不得新增通用Request/Response；不得以Map覆盖重复resource；不得成功/错误统一303或no-store。

## 8. 严格实施步骤

Step 1：AuthorizationConfig/RequestFacts与App context，迁纯parameters/policy/response保护helper。Step 2：PAR/JAR/pushed/reauth完整协议链迁，Adapter保留parser/原证书时机。Step 3：flow/prompt_none/decision迁App，接SessionResolver。Step 4：consent/client_presentation迁并保持原HTTP投影。Step 5：确认所有extension消费者消失，原子删除OAuthJsonErrorFields与写入，回归全部重定向。

## 9. 每一步局部验证

```bash
# Steps 1/2
cargo check --locked -p nazo-oauth-server -p nazo-http-actix -p nazoauth --all-targets
cargo test --locked -p nazo-auth
cargo test --locked -p nazo-oauth-server --lib
# Step 3
cargo test --locked -p nazo-http-actix --test authorization_decision_transport
cargo test --locked -p nazo-http-actix --test form_post_response
# Step 4新增App tests/authorization_application.rs
cargo test --locked -p nazo-oauth-server --test authorization_application
cargo test --locked -p nazoauth --lib framework_boundary_transport
# Step 5
cargo test --locked -p nazo-http-actix --test presenter_contract
python scripts/verify_static_contracts.py --check
rg -n 'OAuthJsonErrorFields|SendCibaResponse' crates
rg -n 'HttpRequest|HttpResponse|actix_|crate::http' crates/authorization-server/src/authorization crates/authorization-server/src/domain/authorization_decision.rs
```

## 10. 任务最终验收标准

App authorization无HTTP/concrete imports；typed error判redirect；两种状态码/form_post/PAR golden通过；OAuthJsonErrorFields定义引用为0；decision业务唯一owner。

## 11. 失败处理

先查redirect授权时机、重复资源丢失、status差异、签名/nonce生成次数和query编码。不能把不安全redirect作为兼容行为保留；若基线问题超出范围明确记录，当前Step回退，不悄改业务规则。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T09.md`。反馈是后续任务唯一需要读取的历史执行摘要。
