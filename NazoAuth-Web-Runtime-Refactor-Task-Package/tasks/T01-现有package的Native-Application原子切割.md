# T01 — 现有package的Native / Application原子切割

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T01-FILE-MAP.md`
- `../references/tasks/T01-INTERFACES.md`
- `../references/CARGO-DEPENDENCY-PLAN.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T00.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T01` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T01.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

让App首先与具体Host脱离，形成可编译的单向package边界。

## 2. 前置条件

P0完成。必须整体切换源文件、测试、Ports、launchers与Cargo，不能先让App依赖Native。

## 3. 精确修改范围

移动E-附表全部原server/src至Native同相对路径；原server/tests的135文件迁Native同相对路径。新增App ports/{mod,persistence,transient_state,fapi_replay}.rs与lib.rs；Native lib.rs、launchers/{mod,postgres,valkey,object_store}.rs。修改三个authorization-server-* Adapter的lib.rs（Object Store含s3.rs）、Native main.rs、这些manifest及根lock；更新两份static脚本和tests/unit路径常量。

## 4. Symbol 级修改方案

F12为唯一launchers切口。ServerPersistenceProvider/Bindings、ServerTransientStateProvider/Bindings、ServerStateBackendBindings、TenantTransientStateFactory、TransientStateHealthPort、TenantDirectoryCachePort及所有原CIBA delivery types归App ports，字段及关联类型不变。FapiHttpSignatureReplayStore及其Consumption/Error归App ports/fapi_replay，future直接std Pin<Box<dyn Future<Output=Result<原结果,原错误>>+Send+'a>>，不依赖尚未迁入的FapiFuture。LauncherFuture/PersistenceLauncher/TransientStateLauncher/AvatarObjectStoreLauncher、ConfigSource、ServerConfigExtension、OperatorPersistence留Native。必要provider accessors公开，无转发wrapper。

## 5. 数据流变化

之前：nazoauth → 混合server → HTTP/Native，PGAdapter → server::bootstrap。
之后：nazoauth(lib+bin) → App ports + concreteAdapters；PG/ValkeyAdapter → App ports；App不依赖Host/Adapter。

## 6. 必须保持的行为不变量

CLI命令、二进制名、环境变量、JSON/schema、provider实例共享、启动顺序、租户绑定和异常退出不变。此Step只有所有权变化，不改路由、安全配置或数据库迁移。

## 7. 禁止实现方式

不得新crate；不得把OperatorPersistence塞入App；不得Adapter→Native；不得留旧server::bootstrap/cli re-export；不得复制整套测试fixture。

## 8. 严格实施步骤

Step 1（原子）：机械移动、Ports提取、launchers迁移、Native入口/Cargo同时闭合。Step 2：更新static guard对Native职责的路径映射及真正受影响的Containerfile源码路径。Step 3：修测试module/fixture相对路径与CARGO_MANIFEST_DIR。Step 4：编译、检查lock、回归所有搬迁测试。

## 9. 每一步局部验证

```bash
# Step 1：本Step唯一允许同步lock的定向check
cargo check -p nazoauth -p nazo-oauth-server-postgres -p nazo-oauth-server-valkey -p nazo-oauth-server-object-store
git diff -- Cargo.lock
# Steps 2–3
cargo check --locked -p nazo-oauth-server -p nazoauth --all-targets
python scripts/verify_static_contracts.py --check
python scripts/check_persistence_dependency_graph.py
cargo test --locked -p nazoauth --lib -- --list
# Step 4
cargo test --locked -p nazoauth --lib
cargo test --locked -p nazo-postgres --test migrations
python -m unittest discover -s tests/unit -v
rg -n 'nazo_oauth_server::(cli|config|operator_task|recovery_root|bootstrap)' crates
```
末条预期无生产命中（rg无命中退出1不是测试失败）。

## 10. 任务最终验收标准

App src仅中立Ports；Native lib/main真实存在；所有launcher定义唯一在Native；Adapter无Host依赖；旧源路径删除；测试装载数量不减少且搬迁回归通过。

## 11. 失败处理

先查环是否源自Launcher仍留Adapter、App lib仍声明Native module，再查private accessor。不得加反向依赖解决。Step1失败应将源+tests+Cargo整体回退，不能在各业务加兼容层。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T01.md`。反馈是后续任务唯一需要读取的历史执行摘要。
