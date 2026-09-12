# T06 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/domain/resource_server.rs` | 365 | 混合package依赖/职责归属需切割 | `App/domain/resource_server.rs + App/ports/fapi_replay.rs + Native/http/mtls.rs` | 拆：FAPI语义/replay内移，连接提取在外 | T01/T06 |
| `authorization-server/src/domain/scim.rs` | 344 | 混合package依赖/职责归属需切割 | `App/domain/scim.rs + Native/adapters/security.rs` | authorizer/cursor/event signer内移；bootstrap hasher在外 | T01/T06 |
| `authorization-server/src/domain/token_management.rs` | 327 | 混合package依赖/职责归属需切割 | `App/domain/token_management.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T06 |
| `authorization-server/src/domain/userinfo.rs` | 391 | 混合package依赖/职责归属需切割 | `App/domain/userinfo.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T06 |
| `authorization-server/src/http/dpop.rs` | 120 | 混合package依赖/职责归属需切割 | `App/security/dpop.rs + Native/http/dpop.rs` | 校验语义内移；headers提取/呈现外置 | T01/T04/T06 |
| `authorization-server/src/http/mtls.rs` | 500 | 混合package依赖/职责归属需切割 | `App/security/mtls.rs + Native/http/mtls.rs` | 纯证书身份验证内移；TLS/proxy/request-cache外置 | T01/T06 |
| `authorization-server/src/http/token/client_auth.rs` | 353 | 混合package依赖/职责归属需切割 | `App/token/client_auth.rs` | 共享认证纯facts/语义；删除Native依赖 | T01/T06 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |

## E2. HTTP Adapter全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `http-actix/src/authorization_request_object.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/cookies.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/cors.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/csrf.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration/ip.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration/response.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/form_post_response.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/lib.rs` | `原文件` | 模块/导出更新，删除旧contract兼容surface | T02/T05/T06/T09 |
| `http-actix/src/middleware.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/scim.rs` | `App/contracts/scim.rs + 原文件` | F1指定symbols内移，其余transport保持 | T06 |
| `http-actix/src/session.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/userinfo.rs` | `App/contracts/userinfo.rs + 原文件` | F1指定symbols内移，其余transport保持 | T06 |
