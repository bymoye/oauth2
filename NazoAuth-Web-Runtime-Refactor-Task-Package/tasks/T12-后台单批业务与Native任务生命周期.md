# T12 — 后台单批业务与Native任务生命周期

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T12-FILE-MAP.md`
- `../references/tasks/T12-INTERFACES.md`
- `../references/CARGO-DEPENDENCY-PLAN.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T03.md`
- `../feedback/T04.md`
- `../feedback/T05.md`
- `../feedback/T10.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T12` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T12.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

Application只处理到期的一批任务；Host拥有调度、网络与停止。

## 2. 前置条件

T03 key生命周期已Native；T04 audit/resolver；T05 logout业务与P10 CIBA业务已中立。

## 3. 精确修改范围

拆原domain/ciba_ping_delivery.rs、backchannel_logout_worker.rs：App workers/{mod,ciba_ping,backchannel_logout}.rs；Native adapters/{ciba_ping_sender,backchannel_logout_sender,ciba_ping_tls}.rs及jobs/{ciba_ping,backchannel_logout}.rs。原domain/ciba_ping_tls.rs整体迁Native。更新Native bootstrap/startup/{background,tenant_runtime}.rs、runtime_modules.rs；audit_anchor/{worker,transport,config}.rs仍Native，仅测试/调度归属核对。

## 4. Symbol 级修改方案

两个worker构造器按F5接原store+sender，process_due_batch返回原Result<usize>；claim/finish/CAS/分类重试留App；sender只返回原status或网络错误。Native spawn函数收Arc<worker>返回JoinHandle<()>，loop维持原节奏。fallible sender构造在spawn前完成。删除Backchannel worker的cfg(not(test))对生产主体遮蔽，单测运行同一业务实现。AuditAnchor现有run_iteration及IterationOutcome保留，不新增App Port。

## 5. 数据流变化

之前：业务worker自己的永久loop/spawn/sleep+HTTP。
之后：Native job → App process_due_batch → store与专用sender能力；Native sender执行DNS/HTTP；App finish/重试；Native等待/下一批/停止。

## 6. 必须保持的行为不变量

CIBA batch8/concurrency8/lease15s，首次立即，完整批次结束后sleep500ms；等待全部item再返回首错，finish Missing/Conflict非fatal。Logout batch20/concurrency8/lease300s，首次立即，完成后sleep5s；200/204完成、408/425/429/5xx重试；5/15/45s及attempts-1索引、expiry严格比较、lastError512字符、fencing保持。DNS仍在原HTTPtimeout之外；CIBA connect3/total5秒，logout3秒；no_proxy/no_redirect/DNS pin/private-origin例外/每条CIBA TLS加载保持。CIBA/logout原abort+await不同于key cooperative stop，不能统一。module1s Skip immediate/drain1s、tenantcache1s/db5s、generation单调/原子发布保持。任务每进程或租户graph一份，不每Actix worker一份。AuditAnchor retry上限300秒、health1秒、genesis顺序、current+remaining后缀重排与原取消语义保持，不新承诺shutdown drain。

## 7. 禁止实现方式

不得RuntimePort/spawn能力；不得batch内部永久loop；不得统一不同worker首次/取消策略；不得把业务retry移sender；不得加数据库写放大；不得为了测试只编译替代worker；不得DNStimeout范围顺便调整。

## 8. 严格实施步骤

Step 1：sender具体实现移Native、App加入两个窄Port并保持原处理逻辑。Step 2：process_due_batch剥离loop，迁App并加fake并发/fencing tests。Step 3：Native jobs接原循环和stop语义，startup保存所有handles。Step 4：核对tenant退役/module排空/key/audit anchor生命周期，pausedclock tests。Step 5：删除旧worker loop位置、cfg遮蔽、无用Cargo，跑原真请求/故障回归。

## 9. 每一步局部验证

```bash
# Steps 1/2
cargo check --locked -p nazo-oauth-server -p nazoauth --all-targets
# 新增App tests/delivery_batches.rs
cargo test --locked -p nazo-oauth-server --test delivery_batches
cargo test --locked -p nazo-oauth-server --lib
# Steps 3/4：对应外置module必须先接入lib的cfg(test)
cargo test --locked -p nazoauth --lib -- --list
cargo test --locked -p nazoauth --lib ciba_ping
cargo test --locked -p nazoauth --lib backchannel_logout
cargo test --locked -p nazoauth --lib key_lifecycle
cargo test --locked -p nazo-runtime-modules
# Step 5
python scripts/verify_static_contracts.py --check
python scripts/check_persistence_dependency_graph.py
rg -n 'tokio::|reqwest::|JoinHandle|spawn|sleep|interval' crates/authorization-server/src/workers
```

## 10. 任务最终验收标准

App worker没有scheduler/network/JoinHandle；process_due_batch可由fake能力驱动并终止；并发/claim/finish/retry原值；Native任务总数与基线一致，退出/退役测试通过；实际worker主体被单测。

## 11. 失败处理

先查批次返回首错是否提前取消其他item、sleep是否被interval取代、stop是否取消keyrefresh、租户切换是否启动重复worker。不得统一取消策略或增补偿层。单个worker迁移失败回退该worker完整Step，保持另一个已完成边界。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T12.md`。反馈是后续任务唯一需要读取的历史执行摘要。
