# T13 性能验收

结论：PASS。生产源码基线 `ff344fc37d36231ac7e648fd24d0bc657643327f`，当前 `33acf5ba54082ac199c250bbe80be5d30ea73c04`。同一 CNB 主机、相同镜像基础、同一数据库/Valkey/密钥/测试向量快照，每轮恢复后按 baseline1/current1 至 baseline5/current5 交替执行。两侧均清理全部 21 个 workspace release 产物后构建，构建不在测量阶段。

硬件：AMD EPYC 9K65，64 online CPU；cgroup CPU quota 6400000、内存上限 128 GiB。使用原 capacity profile 的 `oidc_cold_login_refresh`，8 VUs、shared-iterations 50，每轮 300 HTTP 请求和 50 个完整流程。全部原阈值通过、零错误。配置的 duration 为 20s，但该 executor 实际负载约 1.1s；不能解释为 20 秒稳态、长时稳定性或完整容量曲线。

## 五轮中位数

| 指标 | 基线 | 当前 | 变化 |
|---|---:|---:|---:|
| 吞吐 requests/s | 268.367 | 266.907 | -0.544% |
| P50 ms | 6.364 | 6.554 | +2.986% |
| P95 ms | 134.722 | 134.544 | -0.132% |
| P99 ms | 146.266 | 143.761 | -1.713% |
| 进程 CPU seconds | 6.86 | 6.84 | -0.292% |
| VmRSS bytes | 99454976 | 99586048 | +0.132% |
| PostgreSQL calls | 5897 | 5831 | -1.119% |
| Valkey commands | 2364 | 2363 | -0.042% |
| 签名 backend dispatch attempts | 200 | 200 | +0.000% |

判定采用预先规定的吞吐下降不超过 5%、P99 上升不超过 5%；均满足。[逐轮数值与中位数](PERFORMANCE.json) 保留全部五轮，没有剔除离群轮次。

## 数据含义与复现

- CPU 为 `/proc/1/stat` 的 utime+stime 差值，核对 start_ticks 保证同一进程、tick rate=100、每轮差值大于零；涵盖原 run_scenario 和管理/采样阶段约 2.5s。CNB rootless Docker stats 的 CPU/RSS 零值不可用，不当作实际零消耗。VmRSS 来自 `/proc/1/status` 的一至两次采样，不声称捕获峰值。
- PostgreSQL/Valkey 为原 runner 的 store 统计差值，包含后台工作；小幅调用差异不能据此归因为业务优化。原 pool acquire count 两侧为零，不据此判断池开销。
- 为满足实际签名计数，仅在两个外部测试副本的相同 key-management `sign_selected` 入口加 AtomicU64 Relaxed 计数，并经已有 perf metrics 输出。两侧同样增加一次 atomic RMW；数据来自插桩制品。计数含 dispatch 后失败/取消，非物理外部进程数，也不涵盖所有密码学运算。本场景两侧每轮均为 200，流程成功。生产仓库和原 HTTP 验收制品未插桩。
- 原八项 compose/env/runner/seed/k6/Containerfile/load/SCIM 工作负载的仓库 SHA256 相同。实际外部 harness 为重现基线修正：Compose SQL dollar escaping；专用 volume UID10001 权限；Host 与原 issuer 一致（采用原 real HTTP CI 方式）；seed 显式补齐基线已要求的 security_policy 与 refresh oidc_auth_context；approve 严格断言基线实际 303；跨版本 cargo workspace cache 清理。没有修改 DB 约束、安全默认配置、并发、timeout 或产品代码。
- 每轮恢复相同 PostgreSQL dump、Valkey DUMP/PTTL、runtime/state 文件；恢复后检查 fixture 与 state 哈希。快照含合成测试密钥，保留在本地，不作为公开发布附件。
- 初次五组已测功能/时延但缺有效 CPU，保留为历史证据；发现 CPU 数据不可用后补测的五组配对是本报告唯一判定输入。失败 preflight、原 302 断言失败和 cache build 失败同样保留，不计入通过轮次。

证据根：`D:/self/.worktrees/nazoauth-t13-j4/`。主要数据在 `j4-evidence-clean/cpu-{baseline,current}-run-{1..5}`；`cpu-comparison.json`、`hardware.txt`、`j4-cpu1.log`；实际执行的脚本与补丁在 `j4-tools-final/`、`j4-instrumentation-final/`。各轮 manifest 保存 source SHA、不可变 image ID、参数和 fixture 哈希。canonical state digest 为 `4a18360b7698d1a788dfce550d2657230ed33b06b574242da79216ca071ef382`。
