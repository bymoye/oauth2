# T02 — 中立HTTP / VC contracts归位

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T02-FILE-MAP.md`
- `../references/tasks/T02-INTERFACES.md`
- `../references/CARGO-DEPENDENCY-PLAN.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T01.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T02` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T02.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

移除业务为引用契约而依赖具体HTTP Adapter的方向。

## 2. 前置条件

T01；UserInfo与SCIM含HttpRequest的整组契约延后P6一次迁，不能先内移一个仍需Actix的trait。

## 3. 精确修改范围

F1所有P2 Symbol及其源文件、目标contracts；http-actix/src/lib.rs与Cargo；VC Actix lib/vci/vp，openid4vci/src/{lib,application}.rs、openid4vp/src/{lib,application}.rs及Cargo；删除http-actix/src/request_context.rs；Native域实现的相关imports。

## 4. Symbol 级修改方案

原定义/derive/default methods/Send约束保持。BasicAuthorizationCredentials变public、TransportFacts提供from_parts；parser与TokenClientAuthForm留外层。AccessTokenAuthScheme先迁，UserInfo其他类型P6。VC error.status保留u16。DynamicRegistrationSecurityServices字段为迁移调用暂用pub，P5内部消费完成后收回pub(crate)，不保留双定义。

## 5. 数据流变化

之前：业务impl → http-actix contract。
之后：Actix endpoint → App contract ← 尚在Native等待迁入的业务impl；VC endpoint → VCI/VP owner ← 业务impl。

## 6. 必须保持的行为不变量

全部wire字段、错误码、默认值、future Send/!Send、HTTP extractor时机、cache/header/cookie不变。

## 7. 禁止实现方式

不得迁Endpoint/IpCidr/ActixStatus；不得旧Adapter兼容pub use；不得强加Send；不得新共享web-contracts crate。

## 8. 严格实施步骤

Step 1：身份/session类contract及endpoint/impl import一起迁。Step 2：metadata/runtime/token-management/FAPI/remote JWKS contract。Step 3：client-auth/form facts、AccessTokenAuthScheme/DPoP context。Step 4：分别闭合VCI再VP。Step 5：删除RequestContext、旧导出，建立唯一owner检查。

## 9. 每一步局部验证

```bash
# Steps 1/2/3，每组闭合后执行
cargo check --locked -p nazo-oauth-server -p nazo-http-actix -p nazoauth
cargo test --locked -p nazo-http-actix
# Step 4
cargo test --locked -p nazo-openid4vci -p nazo-openid4vp
cargo test --locked -p nazo-openid4vc-http-actix --test transport_contract
# Step 5
cargo test --locked -p nazoauth --lib
python scripts/verify_static_contracts.py --check
rg -n 'actix_|tokio::|nazoauth::' crates/authorization-server/src/contracts
```
新增manifest依赖先按H同步lock，随后执行以上locked命令。

## 10. 任务最终验收标准

F1已迁Symbol各唯一definition；App contracts无Framework类型；VC Adapter只保留transport-owned定义；Native业务不再从Adapter导入已迁contract；transport tests通过。

## 11. 失败处理

先查derive/alias/private字段是否隐含旧crate类型，再查http0.2/1转换。单能力Step无法闭合即回退该Step；不能App→Adapter或复制定义，不扩大到UserInfo/SCIM。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T02.md`。反馈是后续任务唯一需要读取的历史执行摘要。
