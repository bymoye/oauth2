# T13 最终验收记录

Overall: PASS（T00–T13 重构验收）；发布与部署另行记录。生产代码提交 `33acf5ba54082ac199c250bbe80be5d30ea73c04`；研究基线 `ff344fc37d36231ac7e648fd24d0bc657643327f`。T00–T13 已通过统一验收；K41 官方 OIDF 按用户明确修订交由用户手动执行，状态为 USER-OWNED / NOT RUN。此结论不声称官方认证通过或生产部署完成。

所有下列已通过项对应上述生产代码。验证结束后的任务反馈编辑不改变生产源码；其他任务的工作区改动不进入本次提交或制品。

## 命令和证据

证据文件均在 `D:/self/.worktrees/`。

| ID | 命令或证据 | 结果 |
|---|---|---|
| E1 | T00 baseline SHA、source tree 与 34 项 manifest/lock/CI 摘要核对；`feedback/T00.md`、`docs/project/web-runtime-refactor-baseline.md` | PASS |
| E2 | `cargo fmt --all --check`；`cargo check --locked --workspace --all-targets --all-features`；`cargo clippy --workspace --all-targets --all-features --locked --keep-going -- -D warnings`；`nazoauth-t13-final-gate.log` | exit 0；check 27.37s、clippy 12.80s |
| E3 | `python -m unittest discover -s tests/unit -v`；`nazoauth-t13-python-final3.log` | 137 PASS，5.908s |
| E4 | `python scripts/verify_static_contracts.py --check`；`python scripts/check_persistence_dependency_graph.py`；`nazoauth-t13-static-final.log`、`nazoauth-t13-dependencies.log` | exit 0；115 canonical symbols；21 members；含正例和负例 |
| E5 | Linux `cargo test --workspace --all-features --locked --no-fail-fast`；`nazoauth-t13-linux-docker-full2.log` | exit 0；2889 PASS、0 FAIL、7 原有 ignored；实际 PostgreSQL/Valkey/S3 与多实例、进程树测试 |
| E6 | Windows 同参数 full；`nazoauth-t13-final-gate.log`及 `nazoauth-t13-identity-final-exact-binary.log` | full exit 101：2879 PASS、1 次 DB 连接失败、7 原有 ignored；同次构建身份仓储 binary 36/36 PASS，exit 0。不得把 full 101 改为 0 |
| E7 | `cargo check --locked -p nazo-oauth-server --lib`；`cargo test --locked -p nazo-oauth-server --lib --test application_boundaries --test host_replacement_contract`；`nazoauth-t13-host-independent.log` | exit 0；App 295、boundary 2、外部 consumer 3 PASS |
| E8 | 两平台 `cargo test --workspace --all-features --locked -- --list`；`nazoauth-t13-{final,linux}-test-list.log`；`nazoauth-t13-test-inventory-evidence.md` | 两平台 exit 0；Windows 2887、Linux 2896；9 Unix-only；所有名称差异有映射 |
| E9 | `nazoauth-t13-lock-identity.json`；baseline/current registry/git name/version/source/checksum 比较 | added=[]、removed=[]；21 workspace members |
| E10 | `nazoauth-t13-final-diff-audit.md`；人工逐项 diff 与实际 guards | 无新兼容层、重复 contract、全局生产 lint 静音或 test skip；存储底层与缓存算法保持 |
| E11 | `nazoauth-t13-http-evidence/evidence-baseline` 与 `evidence-current-clean`；原 SCIM、load、Valkey outage | 两侧 workload/cleanup exit 0；SCIM 11 cases；各 5×400 requests/32 concurrency，无请求失败；Valkey outage 的 health/token 均 503；current 清理全部 workspace release 产物后重建并重新通过 |
| E12 | 原 compose/runner/env/seed/k6/load/RFC9967 文件 SHA256；`nazoauth-t13-workload-identity.json` | 8 项全部 baseline/current 相同 |
| E13 | `nazoauth-t13-j4/j4-evidence-clean/cpu-{baseline,current}-run-{1..5}`；`cpu-comparison.json`；[性能报告](PERFORMANCE.md) | 五组配对 PASS；每轮 300 requests / 50 flows / 8 VUs；全部零错误、原阈值通过 |
| E14 | 独立发布工作区 `cargo metadata --locked --offline --no-deps --format-version 1`、两份静态守卫、40 项 release policy/attestation/OCI Python tests | 全部 exit 0；21 members 仅发布版本变为 0.2.16，registry/git 依赖不变 |

## K 清单

各项实施 commit 均为 `33acf5ba`（含其已验证前置提交）。PASS 仅覆盖对应列明的证据边界。

| K | 验收项 | 结果 | 证据 |
|---|---|---|---|
| 01 | archive/SHA、基线及后续 HEAD 区别 | PASS | E1、T00/T01 feedback |
| 02 | workspace 仍为 21 package，无新 App/Host/runtime crate | PASS | E4、E9 |
| 03 | 原 nazoauth binary 与 Native library、CLI/环境入口保持 | PASS | E2、E5、E6、E10 |
| 04 | App 无 Adapter/Host 正常依赖反向边 | PASS | E4、E7 |
| 05 | Host Replacement 可独立构造、调用、终止 | PASS | E7：3 外部消费者用例 |
| 06 | 外部 test 只用 public App 和 semantic ports | PASS | E4、E7 |
| 07 | 真实外层边界，无泛化 runtime/request/host callback | PASS | E4、E7、E10 |
| 08 | F1 canonical 唯一，无旧 Adapter 兼容导出 | PASS | E3、E4：115 symbols |
| 09 | UserInfo/SCIM/FAPI neutral request/context | PASS | E4、E5 |
| 10 | PreparedUserinfo 不可伪造且安全读取一次 | PASS | E5：security_facts 3 cases |
| 11 | 原 Bearer+x5t 证书分支和非法 token 优先级 | PASS | E5：UserInfo transport/security facts |
| 12 | RFC9440 peer CIDR、CA 与绑定策略 | PASS | E5、E6：mTLS、黄金 transport |
| 13 | DPoP present/invalid/duplicate/nonce/replay/htu/htm/ath | PASS | E5、E6、E7 |
| 14 | Token 限流→parse→prepare→certificate→execute | PASS | E5：token_outcome、framework_boundary_transport |
| 15 | Issued/Replayed/PreAuthorized raw bytes/headers | PASS | E5：token_outcome 4 cases、Native golden |
| 16 | SendCibaResponse 删除 | PASS | E4、E10 |
| 17 | OAuthJsonErrorFields/extension 删除、先决定 redirect | PASS | E4、E5、E10 |
| 18 | 无用 RequestContext 删除，无 generic 请求/响应 | PASS | E4、E10 |
| 19 | PAR/JAR/JARM/PKCE/details/resources/redirect/CSRF | PASS | E5、E6：授权/黄金回归 |
| 20 | DCR 四操作、rotation、CAS old hash | PASS | E5：dynamic_registration_application 7 cases |
| 21 | Session amr/auth_time/oidc_sid/MFA/admin/cookie | PASS | E5、E6；内部 prompt-none payload 和公开投影分别验证 |
| 22 | 七个 identity Port Arc 单份直通 | PASS | E4、E5：port_arc_dispatch 7 cases |
| 23 | App service aliases 无 Native concrete types | PASS | E4、E7 |
| 24 | App 无 ConfigSource/settings/env/fs/process/lifecycle | PASS | E4、E7 |
| 25 | Key refresh 保留、Native lifecycle、无 normal Tokio/process-wrap | PASS | E4、E5、E6 |
| 26 | 全外部 signer 路径持 capability、数据格式保持 | PASS | E5、E6、E10 |
| 27 | slot32/deadline/output/子孙清理/本地验签 | PASS | Linux E5、Windows E6；联合坏签名+子孙清理断言保留 |
| 28 | key 首次/退避/stale/in-flight stop | PASS | E5、E6：key_lifecycle |
| 29 | mdoc App payload/验证、Native 执行、pinned lease | PASS | E5：credential_execution_boundaries |
| 30 | CIBA/Logout 单批预算/claim/finish/CAS/retry/expiry | PASS | E5：delivery_batches 6 cases 与 worker unit |
| 31 | Native 时机/sleep/abort+await/graph retire/drain | PASS | E5、E6：jobs/tenant_runtime/runtime_modules |
| 32 | audit 唯一 queue4096/required/tenant/饱和 | PASS | E4、E5、E6、E10 |
| 33 | SnapshotStore 同 Arc、admission 次数和 lease 顺序 | PASS | E5、E6：ptr_eq/调用序列/租户图回归 |
| 34 | PG/Valkey/object store 既有正确边界保持 | PASS | E5、E9、E10；不把 T01 既有 object-store 装配迁移称 byte-identical |
| 35 | 缓存算法保持，无普通库无意义包装 | PASS | E4、E10；JWKS 文本与 ff344fc 旧 owner 相同 |
| 36 | registry/git version/source/checksum 保持 | PASS | E9 |
| 37 | 迁入测试实际装载，App dev 无 Native/Adapter | PASS | E4、E7、E8 |
| 38 | source/dependency 正例与负例 | PASS | E3、E4 |
| 39 | fmt/check/clippy/test 和 static gates | PASS | E2–E8；Windows full 原退出码及同 binary 复验分列 |
| 40 | 原 PG/Valkey/S3/故障/多实例/HTTP matrix | PASS | E5、E6、E11；实际 HTTP current clean build 补验通过 |
| 41 | 官方 OIDF 同配置复测 | USER-OWNED / NOT RUN | 2026-09-12 用户明确跳过，由用户手动执行；不声称认证通过 |
| 42 | 同环境 ≥5 轮性能、CPU/RSS/store/signing | PASS | E12、E13；同快照五组交替配对，吞吐 -0.54%、P99 -1.71% |
| 43 | 最终 diff 无兼容层/重复实现/全局 lint 静音/skip | PASS | E3、E4、E8、E10 |

## 部署

用户授权最终部署至 Hostinger。尚未发布或更新生产；正式制品必须经现有 release-security 信任链，生产更新需新备份/restore-test，并在两个待应用迁移前停止旧 writer。

## 汇总

HostReplacementGate: PASS。DependencyGraph / CanonicalContract / RuntimeOwner / HTTP facts / Protocol regression: PASS，分别见 K04–K38。Performance: PASS，限定于原短场景，见性能报告。External OIDF: USER-OWNED / NOT RUN。Final source: `33acf5ba54082ac199c250bbe80be5d30ea73c04`；后续 ownership 文档提交 `0dbf71399f9d9a2278929a10ee8726de1fb9dabc` 和发布版本元数据不改变已测业务源码。正式发布最终 SHA 与部署结果随后独立记录。

Deviations: 用户允许按依赖连续实施并统一验收；用户接管官方 OIDF；CNB 原环境失效后 Linux 全量改用本机 Docker；最终 HTTP 与性能使用新 CNB。性能所需原 harness 缺陷修正与测量边界逐项列于 PERFORMANCE.md，全部局限于外部测试副本，未放宽产品安全检查。Windows full 101 与同 binary 复验 0 分列；初次缓存污染构建、HTTP/性能 preflight 失败日志保留，不计为通过。
