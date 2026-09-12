# 02 — 执行协议、上下文加载与反馈规则

## 1. 任务包是规范性施工源

本目录是一套可执行任务规格，不是讨论稿。

架构判断、接口归属、依赖方向、迁移顺序、类型设计、禁止项和验收方式已经确定。执行 Agent 的职责是按任务施工与验证，不是重新设计。

## 2. 状态机

任务只允许以下状态：

```text
[ ]  未开始
[-]  执行中
[x]  完成
[!]  阻塞
```

状态唯一登记在 `TASK-INDEX.md`。

规则：

1. 开始任务前：`[ ] -> [-]`。
2. 完成所有步骤、验证与反馈后：`[-] -> [x]`。
3. 出现真实外部阻塞且当前任务无法闭合：`[-] -> [!]`。
4. 未写完整反馈文件，不得标 `[x]`。
5. 后续任务不得绕过未完成的硬前置任务。

## 3. 上下文按需加载协议

### 会话初始化只加载

```text
README.md
00-GOAL.md
01-ARCHITECTURE.md
02-EXECUTION-PROTOCOL.md
TASK-INDEX.md
```

不要一次加载所有 `tasks/`、`references/`、`feedback/`。

### 执行 Txx 时只额外加载

1. `tasks/Txx-*.md`
2. 任务文件“Required Context”列出的 reference 文件
3. 所有直接前置任务对应的 `feedback/Tyy.md`
4. 当前任务实际修改的源码文件

**禁止预读未来任务。**

上下文不足时，优先读取当前任务明确引用的 task-specific reference，而不是重新加载整个任务包。

### 开启新会话继续施工

新会话加载：

```text
README.md
00-GOAL.md
01-ARCHITECTURE.md
02-EXECUTION-PROTOCOL.md
TASK-INDEX.md
当前任务文件
直接前置任务 feedback
当前任务 Required Context
```

历史执行过程不是必需上下文；已完成任务的反馈文件就是规范化交接摘要。

## 4. 每个任务固定执行协议

### Step A — 开始

输出并记录：

```text
Task:
Status:
Baseline commit:
Working tree:
Prerequisite feedback:
Required context loaded:
```

将 TASK-INDEX 状态改成 `[-]`。

### Step B — 按闭合 Step 施工

每个 Step 尽量只完成一个闭合修改：

```text
修改
→ 编译/静态检查
→ 目标测试
→ 记录结果
→ 下一 Step
```

标记“原子”的 Step 必须同时完成 definition、caller、Cargo、tests 的切换。

### Step C — 局部验证

严格执行当前任务列出的命令。

`rg` 无命中可能返回 exit code 1；任务文件明确“预期无结果”的扫描不得被误判为失败。

### Step D — 失败处理

失败时按顺序检查：

1. import / visibility / module 装载；
2. symbol owner 是否仍有双定义；
3. Cargo 是否形成反向依赖；
4. 具体 Framework/Runtime/Host 类型是否仍向内泄漏；
5. 行为顺序是否改变；
6. 测试是否真实装载；
7. 是否属于基线/环境问题。

严禁用以下方式解决：

- Application → Host/Adapter 反向依赖；
- compatibility wrapper/re-export；
- duplicate contract；
- GenericRequest/GenericResponse；
- RuntimePort/Executor；
- `unsafe impl Send` 掩盖 response/runtime 错位；
- skip test；
- 放宽安全检查；
- 增大 timeout/并发掩盖回归。

若当前 Step 无法在既定边界闭合，回退当前 Step，而不是扩大修改范围。

## 5. 每任务反馈是强制制品

任务完成后必须填写：

```text
feedback/Txx.md
```

最少包含：

- 执行前/后 commit；
- 实际修改/移动/删除文件；
- canonical symbol owner 变化；
- Cargo dependency 变化；
- 每条验证命令与 PASS/FAIL/PENDING；
- 行为不变量确认；
- 静态/依赖扫描结果；
- 偏差及原因；
- 未解决风险；
- 下一任务可依赖的最终事实。

填写完成后才能把 `TASK-INDEX.md` 改成 `[x]`。

## 6. 反馈不是过程日志

反馈只记录**可供下一任务消费的稳定事实**。

不要把大量终端输出、完整 diff、推理过程塞进 feedback。必要证据记录命令、摘要、commit、关键路径即可。

## 7. 允许的偏差

只有以下情形允许偏差：

- 实施 HEAD 相比研究基线路径/符号已迁移；
- 编译器/真实代码证明计划中的某个局部路径名称已失效；
- 环境缺失导致某项外部验证不能执行。

偏差必须在 feedback 写：

```text
计划假设：
真实代码：
最小映射：
为什么仍满足 00-GOAL：
验证：
```

不得以“更优雅”“顺手优化”“未来可扩展”为理由偏离架构。

## 8. 完成定义

只有：

```text
T00 ... T13 全部 [x]
+ FINAL-ACCEPTANCE 全部本地可执行项通过
+ Host Replacement Gate 通过
+ 无 compatibility layer / 双定义 / 反向依赖
```

才能宣称任务完成。

Actix/Tokio 字符串减少、目录移动完成、单次 cargo check 通过，都不是完成定义。
