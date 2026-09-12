# T01 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/adapters/audit.rs` | 403 | 混合package依赖/职责归属需切割 | `Native/adapters/audit.rs + App/ports/audit.rs` | 拆：队列/worker在外；显式租户审计契约与纯fields内移 | T01/T04 |
| `authorization-server/src/adapters/audit_anchor/config.rs` | 165 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor/config.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/audit_anchor/preflight.rs` | 77 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor/preflight.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/audit_anchor/protocol.rs` | 84 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor/protocol.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/audit_anchor/status.rs` | 56 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor/status.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/audit_anchor/transport.rs` | 89 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor/transport.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/audit_anchor/worker.rs` | 237 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor/worker.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/audit_anchor.rs` | 25 | 属于外层；原package同时承载业务 | `Native/adapters/audit_anchor.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/avatar_files.rs` | 526 | 属于外层；原package同时承载业务 | `Native/adapters/avatar_files.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/email.rs` | 132 | 属于外层；原package同时承载业务 | `Native/adapters/email.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/email_templates.rs` | 7 | 属于外层；原package同时承载业务 | `Native/adapters/email_templates.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/mod.rs` | 6 | 属于外层；原package同时承载业务 | `Native/adapters/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/adapters/security.rs` | 495 | 混合package依赖/职责归属需切割 | `Native/adapters/security.rs + App/crypto.rs + App/security/client_assertion.rs` | 拆：blocking/hash提取在外，纯token/断言/crypto内移 | T01/T04 |
| `authorization-server/src/bootstrap/authentication_services.rs` | 74 | 混合package依赖/职责归属需切割 | `Native/bootstrap/authentication_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/cors.rs` | 160 | 属于外层；原package同时承载业务 | `Native/bootstrap/cors.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/federation_services.rs` | 101 | 混合package依赖/职责归属需切割 | `Native/bootstrap/federation_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/mod.rs` | 165 | 属于外层；原package同时承载业务 | `Native/bootstrap/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/object_store.rs` | 38 | 属于外层；原package同时承载业务 | `Native/bootstrap/object_store.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/observability.rs` | 197 | 属于外层；原package同时承载业务 | `Native/bootstrap/observability.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/passkey_services.rs` | 64 | 混合package依赖/职责归属需切割 | `Native/bootstrap/passkey_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/persistence.rs` | 135 | 混合package依赖/职责归属需切割 | `App/ports/persistence.rs` | 移动所有provider/bindings定义 | T01 |
| `authorization-server/src/bootstrap/profile_services.rs` | 100 | 混合package依赖/职责归属需切割 | `Native/bootstrap/profile_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/registration_services.rs` | 57 | 混合package依赖/职责归属需切割 | `Native/bootstrap/registration_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/routes.rs` | 594 | 属于外层；原package同时承载业务 | `Native/bootstrap/routes.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/background.rs` | 39 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/background.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/configuration.rs` | 171 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/configuration.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/mod.rs` | 30 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/services/dependencies/openid4vc.rs` | 173 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/services/dependencies/openid4vc.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/services/dependencies.rs` | 253 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/services/dependencies.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/services/factory.rs` | 260 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/services/factory.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/services/identity.rs` | 455 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/services/identity.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/services.rs` | 171 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/services.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/startup/tenant_runtime.rs` | 736 | 属于外层；原package同时承载业务 | `Native/bootstrap/startup/tenant_runtime.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/transient_state.rs` | 190 | 混合package依赖/职责归属需切割 | `App/ports/transient_state.rs` | 移动所有状态Ports/工厂/数据定义 | T01 |
| `authorization-server/src/bootstrap/transport.rs` | 580 | 属于外层；原package同时承载业务 | `Native/bootstrap/transport.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/bootstrap/ui_release.rs` | 299 | 属于外层；原package同时承载业务 | `Native/bootstrap/ui_release.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/cli.rs` | 542 | 属于外层；原package同时承载业务 | `Native/cli.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/config.rs` | 1132 | 属于外层；原package同时承载业务 | `Native/config.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/control_discovery.rs` | 344 | 属于外层；原package同时承载业务 | `Native/control_discovery.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/controller_registry.rs` | 625 | 属于外层；原package同时承载业务 | `Native/controller_registry.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/crypto.rs` | 90 | 混合package依赖/职责归属需切割 | `App/crypto.rs` | 保留原纯RSA/AES实现；P4合并security纯函数 | T01/T04 |
| `authorization-server/src/domain/authorization_decision.rs` | 379 | 混合package依赖/职责归属需切割 | `App/domain/authorization_decision.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T09 |
| `authorization-server/src/domain/backchannel_logout_worker.rs` | 280 | 混合package依赖/职责归属需切割 | `App/workers/backchannel_logout.rs + Native/adapters/backchannel_logout_sender.rs + Native/jobs/backchannel_logout.rs` | 同上；测试编译真实生产主体 | T01/T12 |
| `authorization-server/src/domain/ciba_ping_delivery.rs` | 203 | 混合package依赖/职责归属需切割 | `App/workers/ciba_ping.rs + Native/adapters/ciba_ping_sender.rs + Native/jobs/ciba_ping.rs` | 拆业务批次/具体发送/任务调度 | T01/T12 |
| `authorization-server/src/domain/ciba_ping_tls.rs` | 30 | 属于外层；原package同时承载业务 | `Native/adapters/ciba_ping_tls.rs` | 具体sender TLS装配整体外移 | T01/T12 |
| `authorization-server/src/domain/client_jwe.rs` | 261 | 混合package依赖/职责归属需切割 | `App/domain/client_jwe.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/client_policy.rs` | 62 | 混合package依赖/职责归属需切割 | `App/domain/client_policy.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/dynamic_registration.rs` | 196 | 混合package依赖/职责归属需切割 | `App/domain/dynamic_registration.rs + Native/bootstrap/startup/services/dependencies.rs` | 编排/config/guard内移，Endpoint工厂留Host | T01/T05 |
| `authorization-server/src/domain/jwks_cache.rs` | 191 | 属于外层；原package同时承载业务 | `Native/adapters/jwks_cache.rs` | 随resolver移动，缓存算法保持 | T01/T04 |
| `authorization-server/src/domain/local_registration.rs` | 125 | 混合package依赖/职责归属需切割 | `App/domain/local_registration.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/metadata.rs` | 99 | 混合package依赖/职责归属需切割 | `App/domain/metadata.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/mfa_profile.rs` | 467 | 混合package依赖/职责归属需切割 | `App/domain/mfa_profile.rs + Native/adapters/security.rs` | 操作内移；ServerMfaSecretHasher留Native | T01/T05 |
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/domain/oauth.rs` | 74 | 混合package依赖/职责归属需切割 | `App/domain/oauth.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/oidc_claims.rs` | 380 | 混合package依赖/职责归属需切割 | `App/domain/oidc_claims.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/oidc_logout.rs` | 320 | 混合package依赖/职责归属需切割 | `App/domain/oidc_logout.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/openid4vc/client_attestation.rs` | 235 | 混合package依赖/职责归属需切割 | `App/domain/openid4vc/client_attestation.rs` | 业务整体内移，依赖改中立契约/能力；不复制协议逻辑 | T01/T04 |
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
| `authorization-server/src/domain/passkey.rs` | 155 | 混合package依赖/职责归属需切割 | `App/domain/passkey.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/password_login.rs` | 56 | 混合package依赖/职责归属需切割 | `App/domain/password_login.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/profile_account.rs` | 148 | 混合package依赖/职责归属需切割 | `App/domain/profile_account.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/remote_client_documents.rs` | 302 | 属于外层；原package同时承载业务 | `Native/adapters/remote_client_documents.rs` | 具体DNS/deadline/网络resolver，复用Port | T01/T04 |
| `authorization-server/src/domain/resource_server.rs` | 365 | 混合package依赖/职责归属需切割 | `App/domain/resource_server.rs + App/ports/fapi_replay.rs + Native/http/mtls.rs` | 拆：FAPI语义/replay内移，连接提取在外 | T01/T06 |
| `authorization-server/src/domain/rows.rs` | 4 | 混合package依赖/职责归属需切割 | `App/domain/rows.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/scim.rs` | 344 | 混合package依赖/职责归属需切割 | `App/domain/scim.rs + Native/adapters/security.rs` | authorizer/cursor/event signer内移；bootstrap hasher在外 | T01/T06 |
| `authorization-server/src/domain/sector_identifier.rs` | 142 | 属于外层；原package同时承载业务 | `Native/adapters/sector_identifier.rs` | 具体远程策略/解析随resolver移动 | T01/T04 |
| `authorization-server/src/domain/session_management.rs` | 103 | 混合package依赖/职责归属需切割 | `App/domain/session_management.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/tenancy.rs` | 6 | 混合package依赖/职责归属需切割 | `App/domain/tenancy.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T04 |
| `authorization-server/src/domain/token_management.rs` | 327 | 混合package依赖/职责归属需切割 | `App/domain/token_management.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T06 |
| `authorization-server/src/domain/userinfo.rs` | 391 | 混合package依赖/职责归属需切割 | `App/domain/userinfo.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T06 |
| `authorization-server/src/http/admin/access_requests.rs` | 492 | 属于外层；原package同时承载业务 | `Native/http/admin/access_requests.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/clients/create.rs` | 92 | 属于外层；原package同时承载业务 | `Native/http/admin/clients/create.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/clients/detail.rs` | 45 | 属于外层；原package同时承载业务 | `Native/http/admin/clients/detail.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/clients/list.rs` | 51 | 属于外层；原package同时承载业务 | `Native/http/admin/clients/list.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/clients/mod.rs` | 55 | 属于外层；原package同时承载业务 | `Native/http/admin/clients/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/clients/templates.rs` | 87 | 属于外层；原package同时承载业务 | `Native/http/admin/clients/templates.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/clients/update.rs` | 94 | 属于外层；原package同时承载业务 | `Native/http/admin/clients/update.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/controller_recovery.rs` | 184 | 属于外层；原package同时承载业务 | `Native/http/admin/controller_recovery.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/controller_registry.rs` | 594 | 属于外层；原package同时承载业务 | `Native/http/admin/controller_registry.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/federation.rs` | 83 | 属于外层；原package同时承载业务 | `Native/http/admin/federation.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/grants.rs` | 173 | 属于外层；原package同时承载业务 | `Native/http/admin/grants.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/mtls_trust.rs` | 361 | 属于外层；原package同时承载业务 | `Native/http/admin/mtls_trust.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/openid4vc.rs` | 179 | 属于外层；原package同时承载业务 | `Native/http/admin/openid4vc.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/recovery_root.rs` | 266 | 属于外层；原package同时承载业务 | `Native/http/admin/recovery_root.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin/users.rs` | 450 | 属于外层；原package同时承载业务 | `Native/http/admin/users.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/admin.rs` | 53 | 属于外层；原package同时承载业务 | `Native/http/admin.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/auth/csrf.rs` | 62 | 属于外层；原package同时承载业务 | `Native/http/auth/csrf.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/auth/federation/oidc.rs` | 153 | 属于外层；原package同时承载业务 | `Native/http/auth/federation/oidc.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/auth/federation/saml.rs` | 69 | 属于外层；原package同时承载业务 | `Native/http/auth/federation/saml.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/auth/federation/social.rs` | 284 | 属于外层；原package同时承载业务 | `Native/http/auth/federation/social.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/auth/federation.rs` | 613 | 属于外层；原package同时承载业务 | `Native/http/auth/federation.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/auth/mod.rs` | 4 | 属于外层；原package同时承载业务 | `Native/http/auth/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/authorization/config.rs` | 73 | 混合package依赖/职责归属需切割 | `App/authorization/config.rs + Native/http/authorization/config.rs` | AuthorizationConfig纯字段内移；proxy/configfactory在外 | T01/T09 |
| `authorization-server/src/http/authorization/consent.rs` | 126 | 混合package依赖/职责归属需切割 | `App/authorization/consent.rs + Native/http/authorization/consent.rs` | consent查询/策略内移；csrf投影在外 | T01/T09 |
| `authorization-server/src/http/authorization/jar.rs` | 121 | 混合package依赖/职责归属需切割 | `App/authorization/jar.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/mod.rs` | 122 | 混合package依赖/职责归属需切割 | `App/authorization/mod.rs + Native/http/authorization/mod.rs` | App服务上下文/Operations；Native路由边界 | T01/T09 |
| `authorization-server/src/http/authorization/par.rs` | 603 | 混合package依赖/职责归属需切割 | `App/authorization/par.rs + Native/http/authorization/par.rs` | PAR编排内移，parse/原时序提取留Native | T01/T09 |
| `authorization-server/src/http/authorization/presentation.rs` | 74 | 混合package依赖/职责归属需切割 | `App/authorization/presentation.rs + Native/http/authorization/presentation.rs` | client查询内移；query/error JSON呈现在外 | T01/T09 |
| `authorization-server/src/http/authorization/request/flow.rs` | 590 | 混合package依赖/职责归属需切割 | `App/authorization/request/flow.rs + Native/http/authorization/request/flow.rs` | 协议flow内移；GET/POST handler/extractor在外 | T01/T09 |
| `authorization-server/src/http/authorization/request/form.rs` | 88 | 属于外层；原package同时承载业务 | `Native/http/authorization/request/form.rs` | 保留body/query parser与重复参数处理 | T01/T09 |
| `authorization-server/src/http/authorization/request/mod.rs` | 74 | 混合package依赖/职责归属需切割 | `App/authorization/request/mod.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/request/parameters.rs` | 115 | 混合package依赖/职责归属需切割 | `App/authorization/request/parameters.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/request/policy.rs` | 80 | 混合package依赖/职责归属需切割 | `App/authorization/request/policy.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/request/prompt_none.rs` | 186 | 混合package依赖/职责归属需切割 | `App/authorization/request/prompt_none.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/request/pushed.rs` | 54 | 混合package依赖/职责归属需切割 | `App/authorization/request/pushed.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/request/reauth.rs` | 64 | 混合package依赖/职责归属需切割 | `App/authorization/request/reauth.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/authorization/request/response.rs` | 298 | 混合package依赖/职责归属需切割 | `App/authorization/request/response.rs` | 协议/纯helper内移；父module同步清理 | T01/T09 |
| `authorization-server/src/http/client_attestation.rs` | 37 | 属于外层；原package同时承载业务 | `Native/http/client_attestation.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/dpop.rs` | 120 | 混合package依赖/职责归属需切割 | `App/security/dpop.rs + Native/http/dpop.rs` | 校验语义内移；headers提取/呈现外置 | T01/T04/T06 |
| `authorization-server/src/http/mod.rs` | 13 | 属于外层；原package同时承载业务 | `Native/http/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/mtls.rs` | 500 | 混合package依赖/职责归属需切割 | `App/security/mtls.rs + Native/http/mtls.rs` | 纯证书身份验证内移；TLS/proxy/request-cache外置 | T01/T06 |
| `authorization-server/src/http/perf_metrics.rs` | 9 | 属于外层；原package同时承载业务 | `Native/http/perf_metrics.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/profile/access_requests.rs` | 146 | 属于外层；原package同时承载业务 | `Native/http/profile/access_requests.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/profile/avatar.rs` | 409 | 属于外层；原package同时承载业务 | `Native/http/profile/avatar.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/profile/delivery.rs` | 92 | 属于外层；原package同时承载业务 | `Native/http/profile/delivery.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/profile/federation_links.rs` | 103 | 属于外层；原package同时承载业务 | `Native/http/profile/federation_links.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/profile/mtls_trust.rs` | 130 | 属于外层；原package同时承载业务 | `Native/http/profile/mtls_trust.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/profile.rs` | 11 | 属于外层；原package同时承载业务 | `Native/http/profile.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/http/rate_limit.rs` | 148 | 混合package依赖/职责归属需切割 | `App/rate_limit.rs + Native/http/rate_limit.rs` | 原计数/阈值内移；可信IP/response在外 | T01/T04 |
| `authorization-server/src/http/sessions.rs` | 459 | 混合package依赖/职责归属需切割 | `App/sessions.rs + Native/http/sessions.rs` | SessionResolver/model/policy内移；cookie/CSRF/HTTP在外 | T01/T05 |
| `authorization-server/src/http/token/authorization_code.rs` | 685 | 混合package依赖/职责归属需切割 | `App/token/authorization_code.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/ciba/backchannel.rs` | 375 | 混合package依赖/职责归属需切割 | `App/token/ciba/backchannel.rs + Native/http/token/ciba/backchannel.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/decision.rs` | 350 | 混合package依赖/职责归属需切割 | `App/token/ciba/decision.rs + Native/http/token/ciba/decision.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/policy.rs` | 179 | 混合package依赖/职责归属需切割 | `App/token/ciba/policy.rs` | token polling/policy内移，移除response/request | T01/T07/T08 |
| `authorization-server/src/http/token/ciba/poll.rs` | 418 | 混合package依赖/职责归属需切割 | `App/token/ciba/poll.rs` | token polling/policy内移，移除response/request | T01/T07/T08 |
| `authorization-server/src/http/token/ciba/request.rs` | 428 | 混合package依赖/职责归属需切割 | `App/token/ciba/request.rs + Native/http/token/ciba/request.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/state.rs` | 206 | 混合package依赖/职责归属需切割 | `App/token/ciba/state.rs + Native/http/token/ciba/state.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba.rs` | 113 | 混合package依赖/职责归属需切割 | `App/token/ciba/mod.rs + Native/http/token/ciba.rs` | App业务父模块/Native路由父模块分开 | T01/T08/T10 |
| `authorization-server/src/http/token/client_auth.rs` | 353 | 混合package依赖/职责归属需切割 | `App/token/client_auth.rs` | 共享认证纯facts/语义；删除Native依赖 | T01/T06 |
| `authorization-server/src/http/token/client_credentials.rs` | 182 | 混合package依赖/职责归属需切割 | `App/token/client_credentials.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/device.rs` | 812 | 混合package依赖/职责归属需切割 | `App/token/device.rs + App/contracts/device.rs + Native/http/token/device.rs` | 业务与纯模型内移，parse/CSRF/HTTP保留 | T01/T10 |
| `authorization-server/src/http/token/device_config.rs` | 38 | 混合package依赖/职责归属需切割 | `App/token/device_config.rs + Native/http/token/device_config.rs` | DeviceConfig业务字段内移；HTTP字段在外 | T01/T10 |
| `authorization-server/src/http/token/device_issuance.rs` | 219 | 混合package依赖/职责归属需切割 | `App/token/device_issuance.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/client_auth.rs` | 128 | 混合package依赖/职责归属需切割 | `App/token/dispatch/client_auth.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/errors.rs` | 73 | 混合package依赖/职责归属需切割 | `App/token/dispatch/errors.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/mod.rs` | 688 | 混合package依赖/职责归属需切割 | `App/token/dispatch/mod.rs + Native/http/token/dispatch/mod.rs` | App handles/execute；Native parse/facts/presenter | T01/T07/T08 |
| `authorization-server/src/http/token/dispatch/pre_authorized.rs` | 32 | 混合package依赖/职责归属需切割 | `App/token/dispatch/pre_authorized.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/rate_limit.rs` | 34 | 混合package依赖/职责归属需切割 | `App/token/dispatch/rate_limit.rs + Native/http/token/dispatch/rate_limit.rs` | 业务预算内移；IP输入提取在外 | T01/T08 |
| `authorization-server/src/http/token/issue/authorization_code_state.rs` | 78 | 混合package依赖/职责归属需切割 | `App/token/issue/authorization_code_state.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/issue/refresh_persistence.rs` | 98 | 混合package依赖/职责归属需切割 | `App/token/issue/refresh_persistence.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/issue.rs` | 406 | 混合package依赖/职责归属需切割 | `App/token/issue.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/issue_grant.rs` | 707 | 混合package依赖/职责归属需切割 | `App/token/issue_grant.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/jwt_bearer.rs` | 343 | 混合package依赖/职责归属需切割 | `App/token/jwt_bearer.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/native_sso.rs` | 431 | 混合package依赖/职责归属需切割 | `App/token/native_sso.rs` | P7共享状态helper，P8剩余用例，唯一文件不复制 | T01/T07/T08 |
| `authorization-server/src/http/token/refresh.rs` | 374 | 混合package依赖/职责归属需切割 | `App/token/refresh.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/token_exchange.rs` | 515 | 混合package依赖/职责归属需切割 | `App/token/token_exchange.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token.rs` | 244 | 混合package依赖/职责归属需切割 | `App/token/mod.rs + Native/http/token.rs` | App声明grant服务；Native路由/提取/呈现 | T01/T07/T08 |
| `authorization-server/src/http/views.rs` | 225 | 混合package依赖/职责归属需切割 | `App/authorization/presentation.rs + Native/http/views.rs` | 仅append_query纯helper内移；HTML在外 | T01/T09 |
| `authorization-server/src/http/well_known.rs` | 137 | 属于外层；原package同时承载业务 | `Native/http/well_known.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/keyctl.rs` | 1014 | 属于外层；原package同时承载业务 | `Native/keyctl.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |
| `authorization-server/src/operator_task/admission.rs` | 117 | 属于外层；原package同时承载业务 | `Native/operator_task/admission.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/operator_task/control_journal.rs` | 794 | 属于外层；原package同时承载业务 | `Native/operator_task/control_journal.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/operator_task/execution.rs` | 807 | 属于外层；原package同时承载业务 | `Native/operator_task/execution.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/operator_task/identity.rs` | 236 | 属于外层；原package同时承载业务 | `Native/operator_task/identity.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/operator_task/mod.rs` | 453 | 属于外层；原package同时承载业务 | `Native/operator_task/mod.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/recovery_root.rs` | 335 | 属于外层；原package同时承载业务 | `Native/recovery_root.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/runtime_modules.rs` | 373 | 属于外层；原package同时承载业务 | `Native/runtime_modules.rs` | Native生命周期/registry装配；App使用共享SnapshotStore | T01/T04/T12 |
| `authorization-server/src/settings/config_loader.rs` | 723 | 属于外层；原package同时承载业务 | `Native/settings/config_loader.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/settings/email.rs` | 121 | 属于外层；原package同时承载业务 | `Native/settings/email.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/settings/federation/providers.rs` | 392 | 属于外层；原package同时承载业务 | `Native/settings/federation/providers.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/settings/federation.rs` | 63 | 属于外层；原package同时承载业务 | `Native/settings/federation.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/settings/passkey.rs` | 45 | 属于外层；原package同时承载业务 | `Native/settings/passkey.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/settings/profile.rs` | 161 | 混合package依赖/职责归属需切割 | `Native/settings/profile.rs + App/policy.rs` | from_config改Native freeparser；纯enum/predicate内移 | T01/T04 |
| `authorization-server/src/settings/rate_limit.rs` | 61 | 属于外层；原package同时承载业务 | `Native/settings/rate_limit.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |
| `authorization-server/src/settings.rs` | 601 | 混合package依赖/职责归属需切割 | `Native/settings.rs + App/policy.rs` | 配置读取/密钥加载在外；纯政策常量/枚举内移 | T01/T04 |
| `authorization-server/src/tenant_resource_preparation.rs` | 172 | 属于外层；原package同时承载业务 | `Native/tenant_resource_preparation.rs` | 机械移动后保持Native职责；仅修导入/构造/测试路径 | T01 |

## E3. 其他生产文件的固定修改范围

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| authorization-server-postgres/src/lib.rs | 原文件 + Native/launchers/postgres.rs | provider保留并开放构造；launcher/operator移外 | T01 |
| authorization-server-valkey/src/lib.rs | 原文件 + Native/launchers/valkey.rs | provider/factory保留；新增bindings入口；launcher移外 | T01 |
| authorization-server-object-store/src/lib.rs | 原文件 + Native/launchers/object_store.rs | provider/config/launcher装配移Native | T01 |
| authorization-server-object-store/src/s3.rs | 原文件 | S3实现保持；配置校验唯一公开方法 | T01 |
| nazoauth/src/main.rs | 原文件 | 入口改自身library/launchers，bin名/CLI不变 | T01 |
