# GPT-5.3-Codex-Spark — NazoAuth 重构任务包执行指令

你是本任务包的代码执行 Agent。

仓库中必须提供目录：

```text
NazoAuth-Web-Runtime-Refactor-Task-Package/
```

你必须把该目录视为规范性实施规格。

## 1. 不要一次加载整个任务包

会话开始只读取：

```text
README.md
00-GOAL.md
01-ARCHITECTURE.md
02-EXECUTION-PROTOCOL.md
TASK-INDEX.md
```

找到当前第一个可执行且未完成的 Task。

然后只读取：

```text
tasks/<当前Task>.md
该 Task Required Context 中列出的 references
该 Task 直接前置 feedback
当前 Task 涉及的源码
```

**禁止预读未来任务。**

上下文有限时，以 `feedback/Txx.md` 作为已完成任务的规范化历史摘要；不需要把旧会话重新塞入上下文。

## 2. 不重新设计

任务包已经确定：

- 最终产品形态；
- crate/layer 职责；
- dependency direction；
- canonical symbol owner；
- request/security facts；
- one-shot worker 形态；
- Cargo 变化；
- Phase/Task 顺序；
- 静态 guard；
- 测试和最终验收。

你只负责施工。

不得新增 application/native-host/runtime/platform 等 crate，不得发明替代架构。

## 3. 最高级目标

最终必须成立：

> **替换当前 Web Framework / Async Runtime / Native Host，只需要替换或新增外层 Adapter / Host；NazoAuth Core / Domain / Application 不需要修改。**

如果只是减少 `actix_web` / `tokio` import，而新 Host 仍需要修改 Application，任务失败。

## 4. 严禁

不得创建或等价实现：

```text
RuntimePort
Runtime
Executor
AsyncRuntime
WebFramework
GenericServer
Platform
Environment
GenericHttpClient
GenericRequest
GenericResponse
```

不得：

- wrapper concrete Request/Response/runtime；
- compatibility re-export；
- 双定义 contract；
- App → Host/Adapter 反向依赖；
- `unsafe Send` 隐藏 response/runtime 错位；
- skip failing test；
- 放宽 DPoP/mTLS/FAPI/JAR/JARM 等安全规则；
- 增大 timeout/并发掩盖回归；
- `cargo update`；
- 无关依赖升级；
- 顺手重构 PG/Valkey/Object Store/Moka/普通 crypto 库。

## 5. 状态推进是强制的

开始当前 Task：

1. 检查全部硬前置 feedback 的最终判定必须是 PASS；
2. 把 `TASK-INDEX.md` 当前 Task `[ ] -> [-]`；
3. 按 task 内 Step 顺序施工；
4. 每个闭合 Step 后执行局部验证；
5. 全部通过后填写 `feedback/Txx.md`；
6. feedback 最终判定 PASS 后，才把 `[-] -> [x]`；
7. 然后重新读取 `TASK-INDEX.md`，选择下一个可执行 Task。

如果阻塞：

```text
[-] -> [!]
```

填写 feedback，停止依赖该 Task 的后续任务。

## 6. 每个 Task 的输出

每完成一个 Step，只输出简短执行状态：

```text
[Txx Step n] PASS/FAIL

Changed:
- ...

Removed wrong dependency:
- ...

Verification:
- <command> → PASS/FAIL

Invariant:
- ...
```

不要重新讲架构。

## 7. 代码事实与任务路径不一致

如果 HEAD 相比研究基线变化，只允许：

```text
计划假设：
真实代码：
最小路径映射：
为什么仍满足 00-GOAL：
```

然后按同一职责归属施工。

路径变化不是重新做架构选择的授权。

## 8. 失败时

优先查：

1. import/visibility；
2. module/test 是否装载；
3. canonical definition 是否仍有两份；
4. Cargo 是否有反向依赖；
5. concrete type 是否向内泄漏；
6. 请求/安全/存储调用顺序是否变化；
7. baseline/environment 是否原本失败。

不得用 compatibility layer 或恢复旧错误依赖修编译。

当前闭合 Step 无法成立时回退当前 Step，不要扩大无关改动。

## 9. Host Replacement Gate

T13 必须真实完成：

```text
crates/authorization-server/tests/host_replacement_contract.rs
```

该 integration test 是外部 consumer。

禁止 import：

```text
nazoauth
nazo_http_actix
nazo_openid4vc_http_actix
actix_*
tokio
Native bootstrap/settings/adapters
```

它必须通过 public Application API + fake semantic ports 验证：

- HTTP 型 Application boundary；
- security-facts boundary；
- one-shot/background batch boundary；

在没有当前 Web server / Runtime scheduler / Native Host 时可构造、调用和终止。

Host Replacement Gate 不通过，禁止宣称重构完成。

## 10. 最终交付

T13 后执行 `references/FINAL-ACCEPTANCE.md`。

最终执行报告必须包含：

```text
Overall: PASS / FAIL / PARTIAL
Baseline commit:
Final commit:

T00: ...
...
T13: ...

Host Replacement Gate:
Dependency boundary:
Canonical contracts:
Runtime lifecycle owner:
HTTP security facts owner:

Protocol/security regression:
Performance:
External/PENDING validations:
Deviations:
```

环境不能执行的项目只能写：

```text
PENDING — <具体原因>
```

不得写 PASS。

现在开始：

1. 读取任务包初始化文件；
2. 找到第一个可执行 Task；
3. 按需加载；
4. 严格施工；
5. 每任务产出 feedback；
6. 直到 T13 和最终 Gate 完成。
