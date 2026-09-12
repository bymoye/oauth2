# T11 — OpenID4VC业务与mdoc执行桥

**状态：`[ ]`**

## Required Context

执行本任务前只加载下列任务包文件；不要预读未来任务。

- `../00-GOAL.md`
- `../01-ARCHITECTURE.md`
- `../02-EXECUTION-PROTOCOL.md`
- `../references/tasks/T11-FILE-MAP.md`
- `../references/tasks/T11-INTERFACES.md`
- `../references/CARGO-DEPENDENCY-PLAN.md`
- `../references/STATIC-ARCHITECTURE-GUARDS.md`
- `../references/TEST-REGRESSION-STRATEGY.md`

直接前置任务反馈：
- `../feedback/T02.md`
- `../feedback/T03.md`
- `../feedback/T04.md`

## 状态与反馈契约

开始时将 `TASK-INDEX.md` 中 `T11` 从 `[ ]` 改为 `[-]`。
只有本任务全部验收完成并填写 `feedback/T11.md` 后，才能改为 `[x]`。
若阻塞，改为 `[!]` 并在反馈中记录真实阻塞；不得绕过前置继续后续任务。

---
## 1. 任务目标

VCI/VP编排不依赖Actix；只有真实blocking/runtime签名执行留Native。

## 2. 前置条件

T02 VC contracts已归各自owner；T03 key外部签名中立；T04 crypto/attestation/audit/服务别名就绪。

## 3. 精确修改范围

迁原domain/openid4vc.rs、openid4vc/{credential_crypto,crypto_helpers,proof_validator}.rs及credential_crypto/{certificates,mdoc,sd_jwt,signer}.rs的业务至App；迁domain/openid4vc_endpoints.rs与其helpers/openid4vci目录/openid4vci_dataset/openid4vp至App。新增App ports/mdoc.rs与Native adapters/mdoc_signer.rs；Native startup/services/dependencies.rs注入签名/SecretHashPort；更新VCTransport调用imports。

## 4. Symbol 级修改方案

F4 MdocDocumentSigner只接owned completed DocumentBuilder、pinned Openid4vcSigningLease、certificate_der，返回原IssuerSignedDocument。App保留country/namespace/CBOR/holder/proof/MSO/validity规则及certificate选择；Native AsyncCoseSigner用原Handle/spawn_blocking/block_on做同步签名桥，不重新选key。ServerCredentialIssuerOperations的tx_code hash走已有SecretHashPort，Native注入RegistrationSecretHasher共享全局预算，PasswordHashInput.into_persistence_value。VC服务fields从Data/具体registry改Arc语义依赖。

## 5. 数据流变化

之前：VC domain impl → VC Actix types；mdoc业务内部Handle/spawn_blocking。
之后：VC Actix → VCI/VP contracts ← App业务；App完整builder+lease → MdocDocumentSigner ← Native执行桥；Apptxcode → 原SecretHashPort ← Native预算执行。

## 6. 必须保持的行为不变量

VCI/VP endpoint JSON/status/cache、nonce/attestation/proof/holderbinding、deferred issuance、dataset授权、status/revocation不变。mdoc签名前后的key/certificate同generation，不能刷新后重新取得key。tx_code hash格式/预算/错误映射不变；签名/payload构造次数不增加。

## 7. 禁止实现方式

不得把全部mdoc逻辑迁Host；不得克隆业务DTO替代库builder；不得GenericExecutor或整体crypto redesign；不得升级mdoc库；不得Native bridge再验证/改变protocolpayload；不得App直接spawn_blocking。

## 8. 严格实施步骤

Step 1：MdocDocumentSigner+Native bridge，在同Step替换原mdoc sign执行段。Step 2：VCI offers的tx_code hash注入已有Port，所有构造点更新。Step 3：VC crypto/proof validator及VCI operations完整迁App。Step 4：VP operations/dataset admin迁App，Adapter仅边界。Step 5：清旧Actix/runtime imports、验证generation与凭证interop。

## 9. 每一步局部验证

```bash
# Steps 1/2
cargo check --locked -p nazo-oauth-server -p nazoauth --all-targets
cargo test --locked -p nazo-key-management
cargo test --locked -p nazoauth --lib
# Steps 3/4
cargo test --locked -p nazo-openid4vci -p nazo-openid4vp -p nazo-digital-credentials
cargo test --locked -p nazo-openid4vc-http-actix --test transport_contract
# Step 5新增App tests/credential_execution_boundaries.rs
cargo test --locked -p nazo-oauth-server --test credential_execution_boundaries
python scripts/verify_static_contracts.py --check
rg -n 'tokio::|Handle::current|spawn_blocking|nazo_openid4vc_http_actix|actix_' crates/authorization-server/src/domain/openid4vc* crates/authorization-server/src/ports/mdoc.rs
```

## 10. 任务最终验收标准

App VC无Actix/runtime/concrete execution；mdoc桥不拥有payload规则；credential contract唯一VCI/VPowner；fake signer验证同lease，真实Native签名回归通过。

## 11. 失败处理

先查builder是否不小心borrow request、lease是否重新获取、credential错误是否被简化、tx_code是否新建semaphore。不得搬整套VC业务到Host或加RuntimePort；回退桥/注入的闭合Step，不升级依赖解难题。

---

## 12. 完成反馈

完成本任务后必须填写 `../feedback/T11.md`。反馈是后续任务唯一需要读取的历史执行摘要。
