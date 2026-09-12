# NazoAuth Web Framework / Async Runtime 边界重构任务计划包

## 任务包定位

这是 NazoAuth Web / Runtime 边界重构的**规范性实施任务包**。

它不是一份需要执行模型一次性读完的长文档。任务被拆成 14 个闭合施工单元；执行者按任务加载上下文、完成局部验证并写入反馈，再进入下一个任务。

## 目录

```text
00-GOAL.md
01-ARCHITECTURE.md
02-EXECUTION-PROTOCOL.md
TASK-INDEX.md

tasks/
  T00-...
  ...
  T13-...

references/
  CARGO-DEPENDENCY-PLAN.md
  STATIC-ARCHITECTURE-GUARDS.md
  TEST-REGRESSION-STRATEGY.md
  FINAL-ACCEPTANCE.md
  SYMBOL-AND-INTERFACE-CONTRACTS.md
  FILE-MIGRATION-MAP-FULL.md
  tasks/
    Txx-FILE-MAP.md
    Txx-INTERFACES.md

feedback/
  T00.md
  ...
  T13.md

PROMPT-GPT-5.3-CODEX-SPARK.md
```

## 第一次进入任务包

只读取：

1. `00-GOAL.md`
2. `01-ARCHITECTURE.md`
3. `02-EXECUTION-PROTOCOL.md`
4. `TASK-INDEX.md`
5. 当前任务文件

然后严格按当前任务 `Required Context` 加载 task-specific references 和前置 feedback。

**不要一次加载全部 tasks/references。**

## 任务推进

```text
T00 → T01 → T02
           ├→ T03 → T04 → T05 → T06 → T07 → T08 → T09 → T10
           └──────────────────────────────→ T11
T03/T04/T05/T10 → T12
全部 T00–T12 → T13
```

实际硬前置以 `TASK-INDEX.md` 为准。

每个任务：

```text
[ ] → [-]
加载当前任务上下文
实施 Step
局部验证
填写 feedback/Txx.md
PASS
[-] → [x]
```

## 最终成功标准

不是“去掉 Actix/Tokio”。

唯一最终成功标准是：

> **替换当前 Web Framework / Async Runtime / Native Host 时，只需要新增或替换外层 Adapter / Host；Core / Domain / Application 不修改。**

T13 的 Host Replacement Gate 是对此目标的硬验证。
