# T10 — CIBA / Device创建、查看和授权决定

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T10-FILE-MAP.md`
- `../references/tasks/T10-INTERFACES.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T08.md`
- `../feedback/T09.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T10` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T10.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

将跨设备流程业务从HTTP handlers移入Application，transport只留解析与安全事实提取。

## 2. 前置条件

T08 polling已中立；P9授权与会话可复用；F11 prepared和response结构固定。

## 3. 精确修改范围

Native http/token/ciba/{backchannel,decision,request,state}.rs与ciba.rs拆；App token/ciba/{mod,backchannel,decision,policy,state}.rs；App contracts/ciba.rs。Native http/token/device.rs、device_config.rs拆App token/device.rs、contracts/device.rs与config；Native bootstrap/routes.rs和startup/services/dependencies.rs修改；不要创建不存在的routes/ciba.rs。

## 4. Symbol 级修改方案

PreparedCibaCreation/PreparedDeviceAuthorization按F11检查认证冲突与client_id/hint再暴露form。CibaApplication与DeviceDecisionHandles只持Arc业务依赖，check_admission在原位置；create不重复检查快照。纯forms/claims/replay/view数据移App；HTTP CibaDecisionRequest/DeviceDecisionForm含csrf的wire表单留Native。决定操作接CurrentSession，不接request；CIBA expected_user_id不能由HTTP任意设置None。

## 5. 数据流变化

之前：Actix extractor → handler内admission/认证/仓储/决策/audit/response。
之后：原extractor与admission位置 → prepared语义preflight → Native证书/CSRF/sessionfacts → App create/verification/decide → typed data → 原HTTP JSON/HTML。

## 6. 必须保持的行为不变量

CIBA request-object/hint规则、授予支持、allow_cross_device_flows、idempotency、binding message64字符、TTL/interval、jti原子消费不变。admission与自动extractor相对顺序不变；Device创建limiter先parse。CIBA用户匹配、审计preflight/intent先于decide、决策竞态/过期错误保持。Deviceverification不新增登录要求，成功决定JSON仍success:true。cookies/CSRF/frontendredirect保持。

## 7. 禁止实现方式

不得重复module snapshot check；不得泛化CIBA决定为可任意传expected_user_id；不得create前提前证书到冲突检查前；不得把wire csrf字段直接当业务事实；不得新增默认登录要求。

## 8. 严格实施步骤

Step 1：纯config/forms/views/prepared函数与Native调用。Step 2：CIBA create完整认证/请求对象/审计链迁App。Step 3：CIBA view/decide迁，Native只CSRF/Session/呈现。Step 4：Device create/view/decide迁，固定原limiter/parse/admission。Step 5：清旧helper/handles，跑全部跨设备回归。

## 9. 每一步局部验证

```bash
# Step 1及Steps 2/3/4各闭合操作
cargo check --locked -p nazo-oauth-server -p nazoauth --all-targets
cargo test --locked -p nazo-auth
cargo test --locked -p nazo-oauth-server --lib
cargo test --locked -p nazoauth --lib
# 新增App tests/cross_device_application.rs
cargo test --locked -p nazo-oauth-server --test cross_device_application
# Step 5
cargo test --locked -p nazoauth --lib framework_boundary_transport
python scripts/verify_static_contracts.py --check
rg -n 'HttpRequest|HttpResponse|web::Data|tokio::|crate::http' crates/authorization-server/src/token/ciba crates/authorization-server/src/token/device.rs
```

## 10. 任务最终验收标准

CIBA/Device创建和决策仅App一份；wire models留Native，业务models唯一；admission/store/audit顺序fake断言通过；真实CSRF/HTTP测试保持。

## 11. 失败处理

先查check_admission是否位置变化、CIBA原hint是否漏apply、DeviceVerification是否被新SessionResolver强制登录、required audit是否移到decide后。不能为了编译让App依赖Native session handles；回退当前操作Step。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T10.md`。反馈是后续任务唯一需要读取的历史执行摘要。
