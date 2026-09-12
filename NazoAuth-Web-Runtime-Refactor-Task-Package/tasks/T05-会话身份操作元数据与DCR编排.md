# T05 — 会话、身份操作、元数据与DCR编排

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T05-FILE-MAP.md`
- `../references/tasks/T05-INTERFACES.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T04.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T05` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T05.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

将已中立契约的业务实现迁入App，并把session policy和DCR业务从transport中提取。

## 2. 前置条件

P4完整闭包；SessionResolver先于其消费者。

## 3. 精确修改范围

Native http/sessions.rs拆到App sessions.rs；domain/{local_registration,password_login,passkey,mfa_profile,profile_account,metadata,oidc_logout,session_management,dynamic_registration}.rs迁App。MFA hasher移Native adapters/security.rs。http-actix/src/dynamic_client_registration.rs与子文件types/auth/handlers修改；ip/response保持transport。Native http/auth/mod.rs及子模块、http/federation.rs、http/sessions.rs、startup/services/{identity,dependencies,factory}.rs更新。

## 4. Symbol 级修改方案

SessionResolver/CurrentSession/SessionPayload原数据语义保留；Native只提取cookie/CSRF与presenter。原泛型ServerLocalRegistrationOperations与ServerPasswordLoginOperations保持泛型形状；PasskeyOperationsProvider用P4 alias；MFA现有MfaSecretHashPort实现留Native。MetadataSnapshotSource读同一SnapshotStore/KeyManager，不读Settings。Logout/SessionManagement依赖原语义store/services。DCR按F9迁四操作、唯一config、结果与错误；Native构造Endpoint。

## 5. 数据流变化

之前：DCR Adapter直接编排仓储，Domain反向工厂；session policy接request。
之后：HTTP cookie/header/body/IP → SessionResolver或DynamicRegistrationApplication → 原identity/core/ports → typed结果 → 原presenter。

## 6. 必须保持的行为不变量

Session missing/invalid/pending/inactive/deleted分支、删除副作用不变；admin level>0、recent MFA原0–300s与30s skew/amr/remembered拒绝规则保持。401清session/CSRF两个cookie及Secure/SameSite/Path/expiry不变。DCR POST/PUT admission→JSON→limiter顺序；GET当前token，PUT轮换token与原条件下secret、CAS旧hash，DELETE撤销/审计顺序。logout sid/post_logout_redirect_uri/front/backchannel/iframe origin保持。

## 7. 禁止实现方式

不得SessionHttpRequest；不得只留user_id丢amr/auth_time/sid；不得提高或降低MFA规则；不得PUT不轮换token；不得Domain返回Endpoint；不得JSON/限流换序。

## 8. 严格实施步骤

Step 1：SessionResolver及Native委托/映射。Step 2：registration、password、passkey逐能力迁。Step 3：MFA/profile及Native hasher。Step 4：metadata/logout/session-management及startup。Step 5（原子DCR）：唯一config/结果/业务四操作+四handler一起迁，fake验证CAS/轮换。Step 6：删旧工厂/冗余字段/Cargo。

## 9. 每一步局部验证

```bash
# Steps 1/2各能力闭合后
cargo check --locked -p nazo-oauth-server -p nazo-http-actix -p nazoauth
cargo test --locked -p nazo-oauth-server --lib
cargo test --locked -p nazoauth --lib
cargo test --locked -p nazo-identity
# Step 3
cargo test --locked -p nazo-http-actix --test mfa_profile_transport
# Step 4
cargo test --locked -p nazo-http-actix --test oidc_logout_transport
# Step 5新增App tests/dynamic_registration_application.rs
cargo test --locked -p nazo-oauth-server --test dynamic_registration_application
# Step 6
cargo test --locked -p nazo-http-actix
python scripts/verify_static_contracts.py --check
rg -n 'HttpRequest|HttpResponse|web::Data|nazo_http_actix|ServerMfaSecretHasher' crates/authorization-server/src/domain crates/authorization-server/src/sessions.rs
```

## 10. 任务最终验收标准

业务无Adapter import；DCR四操作唯一App实现、旧config/factory删除；session tests无需Actix，cookie tests仍走真handler；旧registration token失效回归通过。

## 11. 失败处理

先查普通session被误用admin入口、JSON提前、response_types遗漏、CAS expected hash变化。不得把Endpoint/HttpResponse搬回App或复制config；回退当前能力闭合Step。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T05.md`。反馈是后续任务唯一需要读取的历史执行摘要。
