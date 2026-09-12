# J. 测试与回归策略

## J1. 测试归属

基线server/tests共有135个文件。P1按同相对路径迁Native；纯业务测试随后跟生产模块迁App，HTTP/IO测试留Native/Adapter。禁止App dev-depend Native以借fixture，禁止#[path]重编另一层生产源码。保留外置unit module风格，修正相对路径并显式接入；cargo test成功但运行0条目标测试不算验收。

key纯JWK/signature/generation测试留key；进程fixture移Native tests/unit/adapters/external_signer.rs及子目录；调度移Native tests/unit/jobs/key_lifecycle.rs。test_support的语义数据仍留key，改注入fake signer，不整体搬走。

## J2. 已有回归组

| 保护对象 | 基线已有target/命令 | 阶段 |
|---|---|---|
| OAuth/OIDC协议 | cargo test --locked -p nazo-auth | T04、T06–T10、T13 |
| transport | nazo-http-actix下presenter_contract/form_post_response/authorization_decision_transport/token_client_auth_transport/mfa_profile_transport/oidc_logout_transport/client_ip | T02、T05–T10 |
| SCIM安全 | nazo-http-actix的scim_transport；rfc9967_scim_set_e2e.py | T06/T13 |
| VC协议与transport | nazo-openid4vc-http-actix的transport_contract；VCI/VP/digital-credentials测试 | T02/T11 |
| key/mTLS | nazo-key-management的mtls_trust、lib测试 | T03/T06/T11 |
| 原子grant与replay | App/Native拆分后的原token/authorization/CIBA/device测试；full_real_request_load.py | T07–T13 |
| 数据库契约 | nazo-postgres --test migrations及原持久化/KV检查 | T01/T13 |
| Native多实例/控制面 | avatar_shared_storage、operator_task_process、tenant_directory_control_process、tenant_directory_convergence | T01/T03/T12/T13 |
| source/static | verify_static_contracts、check_persistence_dependency_graph、Python unittest、transport_mode_parity --self-test | 每阶段 |

## J3. 固定新增回归

Native tests/unit/http/framework_boundary_transport.rs对真实handler记录status、多值headers（Set-Cookie/WWW-Authenticate）、原body bytes、Location、Port调用顺序。随机值应验证签名/claim/有效期/绑定，不能简单删字段再比较。

必须覆盖：限流与malformed body；auth-source冲突与malformed证书；UserInfo非法token与证书错误的优先级；普通未绑定Bearer携带malformedDPoP；duplicate/empty/nonce/replay/ath/htu；directTLS/RFC9440/untrustedpeer/租户CA热更；DCR PUT CAS后旧token失效；PAR重复resource与扩展；JAR redirect安全；JARM/form_post；CIBA pending/slow_down/terminal/replay；Device CSRF/session；persisted token原始bytes与header差异。

FAPI另测授权失败、signature replay、lookup unavailable的原响应签名策略；capture时机、body exact bytes、Content-Digest、request digest、x-fapi-interaction-id、签名失败空503。只比JSON语义不够。

新增App tests/application_boundaries.rs，用public App API+fake语义Ports和futures_executor::block_on运行代表use-case，不启动Web或Runtime。新增其他test targets按Phase执行，不能冒充基线已有。

## J4. Runtime与性能

Native调度测试用Tokio paused clock（只Native dev/test开启test-util），断言首次时机、批次完成后间隔、in-flight stop行为、retry、MissedTickBehavior。App batch测试使用受控future+active计数，不sleep。密码取消后blocking worker仍持permit；外部signer测试stdin阻塞、过大输出、排队超时、孙进程残留、cancel cleanup、坏签名/kid/alg。Linux进程组与Windows job object均需原生runner；不能只测Linux便宣称Windows通过。

同硬件/镜像/数据/密钥/并发/压缩配置比较基线与重构，≥5轮测吞吐/P50/P95/P99/CPU/RSS/store调用数/签名次数。原400请求/32并发load/race检查不得新增失败。新增性能闸门：中位吞吐下降>5%或P99上升>5%须定位，不能调大timeout/并发掩盖；此5%是计划要求，不是声称基线已有指标。

## J5. OIDF边界

conformance-security.yml实际包含供应链、RFC9967 SCIM SET、load/race、Valkey outage，不等于官方OIDF全套认证。保存原suite版本/plan/variant/脱敏config及结果ID，同配置分别回归directTLS/RFC9440。官方环境/凭证未提供时明确记external conformance pending，不发明cargo test oidf或NazoAuthCtl参数，不把源码扫描替代认证。