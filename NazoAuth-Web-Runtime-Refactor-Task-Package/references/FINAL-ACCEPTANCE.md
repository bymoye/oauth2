# K. 最终完整验收Checklist

以下每一项必须记录实施commit、执行命令、结果或明确阻塞；不能由执行模型只凭代码目测勾选。

- [ ] 原archive/SHA与实施基线一致，未来HEAD变化已单独核对。
- [ ] workspace package数量仍为21，没有新增application/native/runtime/platform crate。
- [ ] nazoauth包含实际Native library+原binary，CLI/环境变量/二进制入口不变。
- [ ] nazo-oauth-server仅包含App/semantic contracts；正常依赖没有local Adapter/Host反向边。
- [ ] **Host Replacement Gate 通过：假设当前 Actix Adapter / Native Host 被替换，Core / Domain / Application 不需要修改。**
- [ ] `host_replacement_contract` 作为外部消费者 integration test 编译并运行，源码不 import Native/Actix/Tokio，只依赖 public Application API + semantic ports。
- [ ] 新 Framework / Runtime / Host 的接入边界已经完整存在于外层；没有为了“可替换”创建 RuntimePort/GenericRequest/GenericResponse/Host callback/compatibility wrapper。
- [ ] F1所有contract各只有一个canonical定义；旧Adapter无兼容pub use。
- [ ] UserInfo/SCIM不接Framework request；FAPI直接复用原neutral request/context。
- [ ] PreparedUserinfo外层不可伪造，decode/audience/tenant/revocation只一次。
- [ ] UserInfo仅原需要的Bearer+x5t分支提取证书；非法token优先级未变化。
- [ ] RFC9440只信任直接peer CIDR，部署CA/租户CA及绑定策略未改变。
- [ ] DPoP proof_present/非法值/重复header/nonce/replay/htu/htm/ath行为不变。
- [ ] Token限流→parse→prepare→certificate→execute顺序已用调用序列断言。
- [ ] Token Issued/Replayed/PreAuthorized各header与body raw bytes差异保持。
- [ ] SendCibaResponse及相关补救转换已删除。
- [ ] OAuthJsonErrorFields与response extension读写已删除，redirect判断在呈现之前。
- [ ] 未使用RequestContext已删除，未创造GenericRequest/GenericResponse。
- [ ] PAR/JAR/JARM/PKCE/授权详情/多resource/registered redirect与CSRF回归通过。
- [ ] DCR四操作在App唯一实现；PUT token/secret轮换与CAS旧hash验证通过。
- [ ] Session的amr/auth_time/oidc_sid及MFA/admin/cookie语义完整保留。
- [ ] 七个已有identity Port Arc转发仅一份，参数结果直通，无额外wrapper。
- [ ] App service aliases不包含Native verifier/SMTP/audit具体类型。
- [ ] App无ConfigSource/Settings/env/filesystem/process/runtime lifecycle API。
- [ ] KeyManager保留refresh，删除run/stop_lifecycle及watch字段；key无normal Tokio/process-wrap。
- [ ] 外部signer全加载/refresh路径始终持能力，外部数据格式external-command不变。
- [ ] 外部signer slot32、全流程deadline、输出上限、子孙进程清理与签名本地验证通过。
- [ ] Key lifecycle首次等待、失败退避、stale边界、stop等待in-flight行为保留。
- [ ] mdoc payload/验证在App，Native仅执行桥，pinned lease未重取。
- [ ] CIBA/Logout单批可终止、并发预算/claim/finish/CAS/retry/expiry保持。
- [ ] Native首次执行/批后sleep/abort+await/graph退役与module drain tests通过。
- [ ] Audit全进程唯一queue4096、required预检/持久化、显式租户及原饱和策略保持。
- [ ] SnapshotStore是原同一Arc，admission读取次数和lease顺序不变。
- [ ] PG/Valkey/objectstore已有正确Port、SQL/schema/Lua/TTL/CAS未重构。
- [ ] Moka与缓存算法不在变更中；普通库未被无意义包装。
- [ ] registry/git依赖版本/source/checksum未因移动变化。
- [ ] 每个迁入测试实际装载；App tests不dev-depend Native/具体Adapter。
- [ ] source/dependency负例fixture全部按预期失败，正例通过。
- [ ] cargo fmt/check/clippy/test与两份static脚本全部通过。
- [ ] 原服务CI（PG/Valkey/S3等）以及故障/多实例matrix通过。
- [ ] 官方OIDF相关suite同配置复测；未执行明确pending，未冒充认证通过。
- [ ] 同硬件≥5轮性能/资源/store调用比较通过，无增大timeout/并发掩盖退化。
- [ ] 最终git diff没有compatibility wrapper、重复实现、全局lint静音或跳过失败测试。


**完成定义：**只有当所有 K 项满足，并且 Host Replacement Gate 证明“替换当前 Framework / Runtime / Host 不需要修改 Core / Domain / Application”时，才允许将本任务状态标记为完成；仅做到 Actix/Tokio import 减少、目录搬迁或静态扫描无命中都不足以完成任务。

# L. 最终验证命令

## L1. 环境前提

在真正实施后的仓库根目录运行。使用rust-toolchain.toml固定版本，不在本任务升级。普通源码静态检查可离线，Cargo依赖缓存/原git依赖下载、libpq等native工具必须可用。完整集成测试依赖原CI服务，不能把缺数据库导致的失败与架构回归混淆。

基线code-quality工作流服务包括PostgreSQL18、Valkey8；DATABASE_URL为postgresql://postgres:postgres@127.0.0.1:5432/oauth，NAZO_AUDIT_TEST_DATABASE_URL为同主机nazo_audit_test，VALKEY_URL为redis://127.0.0.1:6379/0。保留工作流原state epoch、timeout和MinIO/S3配置；不要为了命令能跑改应用默认安全配置。CI secrets/外部OIDF凭证不写进计划或报告。

## L2. 格式、编译、类型、全量测试

```bash
set -euo pipefail

# 在最后一次manifest变更已按H审查并同步Cargo.lock之后执行。
cargo fmt --check
cargo check --locked --workspace --all-targets --all-features
cargo clippy --workspace --all-targets --all-features --locked --keep-going -- -D warnings

python -m compileall -q scripts
python -m unittest discover -s tests/unit -v
python scripts/verify_static_contracts.py --check
python scripts/check_persistence_dependency_graph.py
python scripts/transport_mode_parity.py --self-test
python scripts/rfc9967_scim_set_e2e.py --source-policy-check

cargo test --locked -p nazo-postgres --test migrations pending_migrations_create_all_runtime_module_state_tables
cargo test --workspace --all-features --locked

# 新增target；完成对应Phase后这些文件必须已存在，不能静默skip。
cargo test --locked -p nazo-identity --test port_arc_dispatch
cargo test --locked -p nazo-oauth-server --test application_boundaries
cargo test --locked -p nazo-oauth-server --test host_replacement_contract
cargo test --locked -p nazo-oauth-server --test dynamic_registration_application
cargo test --locked -p nazo-oauth-server --test security_facts
cargo test --locked -p nazo-oauth-server --test token_outcome
cargo test --locked -p nazo-oauth-server --test authorization_application
cargo test --locked -p nazo-oauth-server --test cross_device_application
cargo test --locked -p nazo-oauth-server --test credential_execution_boundaries
cargo test --locked -p nazo-oauth-server --test delivery_batches

# 列表核查：上述用例和Native外置unit modules不得是0条。
cargo test --locked -p nazo-oauth-server --lib -- --list
cargo test --locked -p nazoauth --lib -- --list
cargo test --locked -p nazoauth --lib framework_boundary_transport
cargo test --locked -p nazoauth --lib external_signer
cargo test --locked -p nazoauth --lib key_lifecycle
cargo test --locked -p nazoauth --lib ciba_ping
cargo test --locked -p nazoauth --lib backchannel_logout
```

Windows runner同样执行Native external_signer测试，保护Job对象/取消清理语义。构建服务依赖缺失时先修环境，不能用忽略integration tests宣布验收。

## L3. 依赖与源扫描

```bash
mkdir -p target/refactor-verification
cargo metadata --locked --format-version 1 --no-deps > target/refactor-verification/metadata.json
cargo tree --locked -p nazo-oauth-server --edges normal,build > target/refactor-verification/application-tree.txt
cargo tree --locked -p nazo-key-management --edges normal,build > target/refactor-verification/key-tree.txt

# 以下rg是辅助定位：无命中返回1是预期；若有命中必须读上下文，最终判定由I的role/source guard负责。
rg -n 'actix_web|actix_tls|nazo_http_actix|nazo_openid4vc_http_actix|nazoauth::|tokio::|process_wrap' crates/authorization-server/src crates/key-management/src
rg -n 'SendCibaResponse|OAuthJsonErrorFields' crates
rg -n 'nazo_oauth_server::(cli|config|operator_task|bootstrap)' crates
rg -n 'trait (Runtime|Executor|AsyncRuntime|WebFramework|GenericServer|Platform|Environment|GenericHttpClient|GenericRequest|GenericResponse)\b' crates

git diff --check
git diff -- Cargo.lock
git status --short
```

不要将rg命令直接塞进上一段set -e脚本并把“无命中退出1”误判失败。正式CI用I的脚本按结构判定，不能用`|| true`吞掉真实检查错误。

## L3.1. Host Replacement Gate

```bash
# Application library本身必须可独立构建与测试。
cargo check --locked -p nazo-oauth-server --lib
cargo test --locked -p nazo-oauth-server --lib
cargo test --locked -p nazo-oauth-server --test application_boundaries
cargo test --locked -p nazo-oauth-server --test host_replacement_contract

# 外部消费者测试源码不得偷偷依赖当前Host/Framework/Runtime。
rg -n 'nazoauth|nazo_http_actix|nazo_openid4vc_http_actix|actix_|tokio::|crate::bootstrap|crate::settings|crate::adapters' \
  crates/authorization-server/tests/host_replacement_contract.rs

# 上一条预期无命中（rg退出1）；正式通过/失败仍由静态架构守卫决定。
python scripts/verify_static_contracts.py --check
python scripts/check_persistence_dependency_graph.py
```

Host Replacement Gate 的解释必须固定：

- 不是要求实现第二套生产 Web Server；
- 不是要求把所有外部库抽象成 Port；
- 是要求从一个**独立外部消费者**视角证明 Application 的 public API 已完整，并且依赖方向只向内；
- 如果该 test 必须引用当前 Host/Actix/Tokio 才能构造业务，则重构未完成；
- 如果为了让 test 通过而新增万能 runtime/request abstraction，同样判定失败。

## L4. 真实服务、故障与官方suite

复用`.github/workflows/code-quality.yml`、`.github/workflows/conformance-security.yml`中的实际部署/environment和`full_real_request_load.py`、`rfc9967_scim_set_e2e.py`的原调用参数。它们有真实证书/租户/状态依赖，不能在计划中发明一个通用命令代替。源码布局变化只更新相应package/fixture路径，不改load/race/outage阈值。

官方OIDF运行需要既有外部suite plan/variant/config；将其原命令/结果ID填入P0基线后，同参数回归。没有提供的外部入口不猜CLI。未执行的OIDF/Windows/性能结果应写“未运行/受环境阻塞”，不能写“通过”。

# M. 改动规模与风险

以下为计划级估计，不是已经实施的diff。纯移动按Git rename理解，不把删除旧路径/新增新路径的两份LOC相加当新业务代码。

| 类别 | 预计量级 | 说明 |
|---|---|---|
| 纯文件移动/import | 原server182个生产文件、135个tests/support文件是P1主要包边界移动 | 后续业务回迁App；部分文件拆分，最终文件数不等于搬迁动作数 |
| Cargo变更 | 约10–13份manifest与Cargo.lock | 无新workspace member；local dependency方向/feature用途移动 |
| 中立contract迁移 | F1清单所列全部定义 | 多数只改owner/import；UserInfo/SCIM需要签名改变 |
| 真正逻辑分离 | 约35–60个生产文件 | token/authorization/安全facts/DCR/mdoc/key/worker是主要区域 |
| 新增生产代码 | 粗估1000–2500行 | 专用facts/outcome/少数已有缺口Port、Native桥、显式构造与有限Arc转发 |
| 删除或替换生产代码 | 粗估1000–2500行，不含机械移动 | 原request/response补救层、重复config/model、旧位置loop/导出 |
| 测试与静态守卫新增 | 粗估1000–3000行 | 具体案例数量依现有fixture可复用量；不为复用引入框架 |
| 总影响路径 | 约360–450个既有/新增路径 | 含测试、父模块、Cargo、CI/源策略；Git rename识别会影响统计 |

“逻辑完全不变”不等于没有风险。最高风险为：①证书/限流/解析/断言consume顺序；②token回放原字节、headers与Send闭包；③JAR错误重定向与JARM/form_post；④租户图/快照/签名lease固定；⑤外部进程全流程deadline和子孙清理；⑥worker取消/批次重试/lease fencing；⑦测试搬迁后未被装载。

顺序上的风险控制：P1只机械切割；P2先解决contractowner；T03–P4建立完整语义依赖闭包；P6安全facts先于token/授权业务迁移；P7先闭合返回类型再迁grant；P12最后拆worker执行与调度；P13不接受通过增加兼容层补洞。