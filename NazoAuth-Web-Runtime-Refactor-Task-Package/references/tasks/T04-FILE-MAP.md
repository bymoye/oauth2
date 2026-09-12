# T04 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/adapters/audit.rs` | 403 | 混合package依赖/职责归属需切割 | `Native/adapters/audit.rs + App/ports/audit.rs` | 拆：队列/worker在外；显式租户审计契约与纯fields内移 | T01/T04 |
| `authorization-server/src/adapters/security.rs` | 495 | 混合package依赖/职责归属需切割 | `Native/adapters/security.rs + App/crypto.rs + App/security/client_assertion.rs` | 拆：blocking/hash提取在外，纯token/断言/crypto内移 | T01/T04 |
| `authorization-server/src/bootstrap/authentication_services.rs` | 74 | 混合package依赖/职责归属需切割 | `Native/bootstrap/authentication_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/federation_services.rs` | 101 | 混合package依赖/职责归属需切割 | `Native/bootstrap/federation_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/passkey_services.rs` | 64 | 混合package依赖/职责归属需切割 | `Native/bootstrap/passkey_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/profile_services.rs` | 100 | 混合package依赖/职责归属需切割 | `Native/bootstrap/profile_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/registration_services.rs` | 57 | 混合package依赖/职责归属需切割 | `Native/bootstrap/registration_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/crypto.rs` | 90 | 混合package依赖/职责归属需切割 | `App/crypto.rs` | 保留原纯RSA/AES实现；P4合并security纯函数 | T01/T04 |
| `authorization-server/src/domain/client_jwe.rs` | 261 | 混合package依赖/职责归属需切割 | `App/domain/client_jwe.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/client_policy.rs` | 62 | 混合package依赖/职责归属需切割 | `App/domain/client_policy.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/jwks_cache.rs` | 191 | 属于外层；原package同时承载业务 | `Native/adapters/jwks_cache.rs` | 随resolver移动，缓存算法保持 | T01/T04 |
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/domain/oauth.rs` | 74 | 混合package依赖/职责归属需切割 | `App/domain/oauth.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/oidc_claims.rs` | 380 | 混合package依赖/职责归属需切割 | `App/domain/oidc_claims.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/openid4vc/client_attestation.rs` | 235 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/client_attestation.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T04 |
| `authorization-server/src/domain/remote_client_documents.rs` | 302 | 属于外层；原package同时承载业务 | `Native/adapters/remote_client_documents.rs` | 具体DNS/deadline/网络resolver，复用Port | T01/T04 |
| `authorization-server/src/domain/rows.rs` | 4 | 混合package依赖/职责归属需切割 | `App/domain/rows.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/sector_identifier.rs` | 142 | 属于外层；原package同时承载业务 | `Native/adapters/sector_identifier.rs` | 具体远程策略/解析随resolver移动 | T01/T04 |
| `authorization-server/src/domain/tenancy.rs` | 6 | 混合package依赖/职责归属需切割 | `App/domain/tenancy.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/http/dpop.rs` | 120 | 混合package依赖/职责归属需切割 | `App/security/dpop.rs + Native/http/dpop.rs` | 校验语义内移；headers提取/呈现外置 | T01/T04/T06 |
| `authorization-server/src/http/rate_limit.rs` | 148 | 混合package依赖/职责归属需切割 | `App/rate_limit.rs + Native/http/rate_limit.rs` | 原计数/阈值内移；可信IP/response在外 | T01/T04 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |
| `authorization-server/src/runtime_modules.rs` | 373 | 属于外层；原package同时承载业务 | `Native/runtime_modules.rs` | Native生命周期/registry装配；App使用共享SnapshotStore | T01/T04/T12 |
| `authorization-server/src/settings/profile.rs` | 161 | 混合package依赖/职责归属需切割 | `Native/settings/profile.rs + App/policy.rs` | from_config改Native freeparser；纯enum/predicate内移 | T01/T04 |
| `authorization-server/src/settings.rs` | 601 | 混合package依赖/职责归属需切割 | `Native/settings.rs + App/policy.rs` | 配置读取/密钥加载在外；纯政策常量/枚举内移 | T01/T04 |
