# T02 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |

## E2. HTTP Adapter全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `http-actix/src/authorization_decision.rs` | `App/contracts/authorization_decision.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/authorization_request_object.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/cookies.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/cors.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/csrf.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dpop.rs` | `App/contracts/request_facts.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/dynamic_client_registration/ip.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration/response.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/dynamic_client_registration/types.rs` | `App/contracts/dynamic_client_registration.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/extract.rs` | `App/contracts/userinfo.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/fapi_resource.rs` | `App/contracts/fapi_resource.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/form_post_response.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/lib.rs` | `原文件` | 模块/导出更新，删除旧contract兼容surface | T02/T05/T06/T09 |
| `http-actix/src/local_registration.rs` | `App/contracts/local_registration.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/metadata.rs` | `App/contracts/metadata.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/mfa_profile.rs` | `App/contracts/mfa_profile.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/middleware.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/oidc_logout.rs` | `App/contracts/oidc_logout.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/passkey.rs` | `App/contracts/passkey.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/password_login.rs` | `App/contracts/password_login.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/profile_account.rs` | `App/contracts/profile_account.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/request_context.rs` | `删除文件/module/export` | 零消费者，不新建通用request | T02 |
| `http-actix/src/runtime_modules.rs` | `App/contracts/runtime_modules.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/session.rs` | `原文件` | 保持transport，仅更新已迁types的imports（如有） | T02/T05/T06 |
| `http-actix/src/session_management.rs` | `App/contracts/session_management.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/token_client_auth.rs` | `App/contracts/token_client_auth.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/token_forms.rs` | `App/contracts/token_forms.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
| `http-actix/src/token_management.rs` | `App/contracts/token_management.rs + 原文件` | F1指定symbols内移，其余transport保持 | T02 |
