# TASK-INDEX — NazoAuth Web / Runtime 边界重构

状态：`[ ]` 未开始；`[-]` 执行中；`[x]` 完成；`[!]` 阻塞。

| 状态 | Task | 任务 | 硬前置 | 执行文件 | 完成反馈 |
|---|---|---|---|---|---|
| [x] | T00 | 锁定代码与行为基线 | 无 | `tasks/T00-锁定代码与行为基线.md` | `feedback/T00.md` |
| [x] | T01 | 现有package的Native / Application原子切割 | T00 | `tasks/T01-现有package的Native-Application原子切割.md` | `feedback/T01.md` |
| [x] | T02 | 中立HTTP / VC contracts归位 | T01 | `tasks/T02-中立HTTP-VC-contracts归位.md` | `feedback/T02.md` |
| [x] | T03 | Key Management语义refresh与Native执行分离 | T01, T02 | `tasks/T03-Key-Management语义refresh与Native执行分离.md` | `feedback/T03.md` |
| [x] | T04 | 共享服务别名、配置、快照与能力闭包 | T01, T02, T03 | `tasks/T04-共享服务别名配置快照与能力闭包.md` | `feedback/T04.md` |
| [x] | T05 | 会话、身份操作、元数据与DCR编排 | T04 | `tasks/T05-会话身份操作元数据与DCR编排.md` | `feedback/T05.md` |
| [x] | T06 | UserInfo / FAPI / SCIM / mTLS / 客户端认证 | T02, T04, T05 | `tasks/T06-UserInfo-FAPI-SCIM-mTLS-客户端认证.md` | `feedback/T06.md` |
| [x] | T07 | Token结果闭包与共享签发语义 | T04, T06 | `tasks/T07-Token结果闭包与共享签发语义.md` | `feedback/T07.md` |
| [x] | T08 | Token各Grant与Dispatcher迁入Application | T06, T07 | `tasks/T08-Token各Grant与Dispatcher迁入Application.md` | `feedback/T08.md` |
| [x] | T09 | Authorization / PAR / JAR / JARM与决策迁移 | T04, T05, T06, T07, T08 | `tasks/T09-Authorization-PAR-JAR-JARM与决策迁移.md` | `feedback/T09.md` |
| [x] | T10 | CIBA / Device创建、查看和授权决定 | T08, T09 | `tasks/T10-CIBA-Device创建查看和授权决定.md` | `feedback/T10.md` |
| [x] | T11 | OpenID4VC业务与mdoc执行桥 | T02, T03, T04 | `tasks/T11-OpenID4VC业务与mdoc执行桥.md` | `feedback/T11.md` |
| [x] | T12 | 后台单批业务与Native任务生命周期 | T03, T04, T05, T10 | `tasks/T12-后台单批业务与Native任务生命周期.md` | `feedback/T12.md` |
| [-] | T13 | 静态守卫、全量回归与删除遗留 | T00, T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12 | `tasks/T13-静态守卫全量回归与删除遗留.md` | `feedback/T13.md` |

## 执行规则

2026-09-12 用户修订：后续按依赖连续实施，完整回归统一验收，避免重复测试。实现闭合的前置允许后继开始；必要编译和接口检查用于及时发现错误。`[-]` 可表示“实现完成，待统一验收”，各反馈必须区分实现与验收状态，统一验收 PASS 后才能标 `[x]`。其余架构、行为与质量要求不变。

1. 只能执行所有硬前置均为 `[x]` 的任务。
2. 每次只将一个任务置为 `[-]`；不要并行修改存在写冲突或依赖关系的任务。
3. 任务 `[x]` 的必要条件是该任务 feedback 最终判定为 PASS。
4. T13 完成后还必须按 `references/FINAL-ACCEPTANCE.md` 完成最终 Gate。
