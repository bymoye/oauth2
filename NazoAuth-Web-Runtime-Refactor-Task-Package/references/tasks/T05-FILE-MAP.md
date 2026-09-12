# T05 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/bootstrap/authentication_services.rs` | 74 | 混合package依赖/职责归属需切割 | `Native/bootstrap/authentication_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/federation_services.rs` | 101 | 混合package依赖/职责归属需切割 | `Native/bootstrap/federation_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/passkey_services.rs` | 64 | 混合package依赖/职责归属需切割 | `Native/bootstrap/passkey_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/profile_services.rs` | 100 | 混合package依赖/职责归属需切割 | `Native/bootstrap/profile_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/bootstrap/registration_services.rs` | 57 | 混合package依赖/职责归属需切割 | `Native/bootstrap/registration_services.rs + App/services.rs` | Native concrete实现/factory留；仅纯alias与业务TTL内移 | T01/T04/T05 |
| `authorization-server/src/domain/dynamic_registration.rs` | 196 | 混合package依赖/职责归属需切割 | `App/domain/dynamic_registration.rs + Native/bootstrap/startup/services/dependencies.rs` | 编排/config/guard内移，Endpoint工厂留Host | T01/T05 |
| `authorization-server/src/domain/local_registration.rs` | 125 | 混合package依赖/职责归属需切割 | `App/domain/local_registration.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/metadata.rs` | 99 | 混合package依赖/职责归属需切割 | `App/domain/metadata.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/mfa_profile.rs` | 467 | 混合package依赖/职责归属需切割 | `App/domain/mfa_profile.rs + Native/adapters/security.rs` | 操作内移；ServerMfaSecretHasher留Native | T01/T05 |
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/domain/oidc_logout.rs` | 320 | 混合package依赖/职责归属需切割 | `App/domain/oidc_logout.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/passkey.rs` | 155 | 混合package依赖/职责归属需切割 | `App/domain/passkey.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/password_login.rs` | 56 | 混合package依赖/职责归属需切割 | `App/domain/password_login.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/profile_account.rs` | 148 | 混合package依赖/职责归属需切割 | `App/domain/profile_account.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/domain/session_management.rs` | 103 | 混合package依赖/职责归属需切割 | `App/domain/session_management.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T05 |
| `authorization-server/src/http/sessions.rs` | 459 | 混合package依赖/职责归属需切割 | `App/sessions.rs + Native/http/sessions.rs` | SessionResolver/model/policy内移；cookie/CSRF/HTTP在外 | T01/T05 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |

## E2. HTTP Adapter全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `http-actix/src/authorization_request_object.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/cookies.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/cors.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/csrf.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration/auth.rs` | `App/domain/dynamic_registration.rs + 原文件` | 四操作业务及纯auth内移，HTTP边界保持 | T05 |
| `http-actix/src/dynamic_client_registration/handlers.rs` | `App/domain/dynamic_registration.rs + 原文件` | 四操作业务及纯auth内移，HTTP边界保持 | T05 |
| `http-actix/src/dynamic_client_registration/ip.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration/response.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration.rs` | `App/domain/dynamic_registration.rs + 原文件` | 四操作业务及纯auth内移，HTTP边界保持 | T05 |
| `http-actix/src/form_post_response.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/lib.rs` | `原文件` | 模块/导出更新，删除旧contract兼容surface | T02/T05/T06/T09 |
| `http-actix/src/middleware.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/session.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
