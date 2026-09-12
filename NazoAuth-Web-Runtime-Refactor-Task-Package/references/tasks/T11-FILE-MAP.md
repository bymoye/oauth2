# T11 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/domain/openid4vc/credential_crypto/certificates.rs` | 193 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/credential_crypto/certificates.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc/credential_crypto/mdoc.rs` | 528 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/credential_crypto/mdoc.rs + Native/adapters/mdoc_signer.rs` | 规则/builder内移；执行桥外置 | T01/T11 |
| `authorization-server/src/domain/openid4vc/credential_crypto/sd_jwt.rs` | 245 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/credential_crypto/sd_jwt.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc/credential_crypto/signer.rs` | 53 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/credential_crypto/signer.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc/credential_crypto.rs` | 48 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/credential_crypto.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc/crypto_helpers.rs` | 212 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/crypto_helpers.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc/proof_validator.rs` | 300 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/proof_validator.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc.rs` | 14 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/helpers.rs` | 318 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/helpers.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/openid4vci/dataset.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/openid4vci/dataset.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/openid4vci/issuance.rs` | 343 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/openid4vci/issuance.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/openid4vci/mod.rs` | 592 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/openid4vci/mod.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/openid4vci/offers.rs` | 456 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/openid4vci/offers.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/openid4vci_dataset.rs` | 271 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/openid4vci_dataset.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints/openid4vp.rs` | 804 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints/openid4vp.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/domain/openid4vc_endpoints.rs` | 14 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc_endpoints.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T11 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |
