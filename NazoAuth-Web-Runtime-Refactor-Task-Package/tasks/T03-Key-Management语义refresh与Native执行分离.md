# T03 — Key Management语义refresh与Native执行分离

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T03-FILE-MAP.md`
- `../references/tasks/T03-INTERFACES.md`
- `../references/CARGO-DEPENDENCY-PLAN.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T01.md`
- `../feedback/T02.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T03` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T03.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

密钥服务不再知道任务循环、shutdown、进程执行或Runtime。

## 2. 前置条件

T01–T02，Native可持KeyManager；需同步所有数据库key加载和刷新路径。

## 3. 精确修改范围

修改key-management/src/{lib,model,database,external,lifecycle,test_support}.rs；新增external_signer.rs。Native新增adapters/external_signer.rs、jobs/{mod,key_lifecycle}.rs；修改Native settings.rs、bootstrap/startup/{background,tenant_runtime}.rs、bootstrap/startup/services/dependencies.rs、keyctl.rs及其子模块、operator_task/execution.rs。迁相关key进程/调度tests与Cargo。

## 4. Symbol 级修改方案

F4 ExternalKeySigner为唯一窄能力。KeySettings仅留三个语义时间字段；ExternalSigningKey持key_ref+Arc<dyn ExternalKeySigner>。ActiveSigningKey::ExternalCommand改External，但数据库backend字符串external-command保持。load_or_create_database、DatabaseKeysetBinding及所有load_record/load_payload/update/list/validate/refresh路径传Option<Arc<dyn ExternalKeySigner>>，不能刷新后丢失。ExternalBackend保留原公钥/JWK/alg本地验证，签名失败仍映SignError::SigningFailed。Native CommandExternalKeySigner接原JSON/slot/deadline/process实现。删除KeyManagerInner.watch字段及run/stop_lifecycle；lifecycle.rs只留stale常量/all_signing_purposes。

## 5. 数据流变化

之前：KeyManager loop/watch → refresh；ExternalBackend → Tokio进程。
之后：Native KeyLifecycleTask → KeyManager.refresh；ExternalBackend → ExternalKeySigner ← Native CommandExternalKeySigner。

## 6. 必须保持的行为不变量

首次等normal interval后refresh；prepublish/2 clamp1–3600秒，VC材料时≤30秒；失败1秒倍增到60秒、成功reset。stop只打断等待、不取消in-flight refresh。2h snapshot stale、60s VC revocation freshness、8次CAS预算、purpose/kid/alg/lease保持。外部signer slots32，全流程deadline在acquire前建立覆盖queue/write/read/wait；stdout64KiB/stderr8KiB、version1 JSON、Unix进程组/Windows job对象、KillOnDrop、正常及取消清理子孙、reaper5秒保持。

## 7. 禁止实现方式

不得新Runtime/Executor；不得每次sign建semaphore；不得只kill child；不得移除本地公钥验证；不得将整个Signer改dyn；不得改变schema或stale健康策略。

## 8. 严格实施步骤

Step 1：ExternalKeySigner、Native执行、所有database加载/构造路径一次闭合。Step 2：loop/watch/stop归Native，同时更新tenant退休与operator调用。Step 3：拆tests，key用fake signer，进程/调度真实实现留Native测试。Step 4：删key normal Tokio/process-wrap并跑平台取消/超时。

## 9. 每一步局部验证

```bash
# Steps 1/2
cargo check --locked -p nazo-key-management -p nazoauth --all-targets
cargo test --locked -p nazo-key-management --lib
# Step 3
cargo test --locked -p nazo-key-management --test mtls_trust
cargo test --locked -p nazoauth --lib -- --list
cargo test --locked -p nazoauth --lib external_signer
cargo test --locked -p nazoauth --lib key_lifecycle
# Step 4；Windows runner也执行external_signer过滤测试
rg -n 'tokio::|process_wrap|run_lifecycle|stop_lifecycle|std::process::Command' crates/key-management/src
python scripts/verify_static_contracts.py --check
```

## 10. 任务最终验收标准

key生产无Tokio/process lifecycle和正常依赖；外部能力唯一owner为key；Native完整持有任务到退出；旧external-command数据无需migration；平台IO/取消tests实际运行。

## 11. 失败处理

先查binding漏传signer、backend仍持command、fixture引用Native私有字段。外部key缺能力必须fail-closed。不得恢复watch/Tokio feature；回退当前接口Step，停止算法/schema扩大重构。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T03.md`。反馈是后续任务唯一需要读取的历史执行摘要。
