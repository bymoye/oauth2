# T08 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/http/token/authorization_code.rs` | 685 | 混合package依赖/职责归属需切割 | `App/token/authorization_code.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/ciba/backchannel.rs` | 375 | 混合package依赖/职责归属需切割 | `App/token/ciba/backchannel.rs + Native/http/token/ciba/backchannel.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/decision.rs` | 350 | 混合package依赖/职责归属需切割 | `App/token/ciba/decision.rs + Native/http/token/ciba/decision.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/policy.rs` | 179 | 混合package依赖/职责归属需切割 | `App/token/ciba/policy.rs` | token polling/policy内移，移除response/request | T01/T07/T08 |
| `authorization-server/src/http/token/ciba/poll.rs` | 418 | 混合package依赖/职责归属需切割 | `App/token/ciba/poll.rs` | token polling/policy内移，移除response/request | T01/T07/T08 |
| `authorization-server/src/http/token/ciba/request.rs` | 428 | 混合package依赖/职责归属需切割 | `App/token/ciba/request.rs + Native/http/token/ciba/request.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/state.rs` | 206 | 混合package依赖/职责归属需切割 | `App/token/ciba/state.rs + Native/http/token/ciba/state.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba.rs` | 113 | 混合package依赖/职责归属需切割 | `App/token/ciba/mod.rs + Native/http/token/ciba.rs` | App业务父模块/Native路由父模块分开 | T01/T08/T10 |
| `authorization-server/src/http/token/client_credentials.rs` | 182 | 混合package依赖/职责归属需切割 | `App/token/client_credentials.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/device_issuance.rs` | 219 | 混合package依赖/职责归属需切割 | `App/token/device_issuance.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/client_auth.rs` | 128 | 混合package依赖/职责归属需切割 | `App/token/dispatch/client_auth.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/errors.rs` | 73 | 混合package依赖/职责归属需切割 | `App/token/dispatch/errors.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/mod.rs` | 688 | 混合package依赖/职责归属需切割 | `App/token/dispatch/mod.rs + Native/http/token/dispatch/mod.rs` | App handles/execute；Native parse/facts/presenter | T01/T07/T08 |
| `authorization-server/src/http/token/dispatch/pre_authorized.rs` | 32 | 混合package依赖/职责归属需切割 | `App/token/dispatch/pre_authorized.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/dispatch/rate_limit.rs` | 34 | 混合package依赖/职责归属需切割 | `App/token/dispatch/rate_limit.rs + Native/http/token/dispatch/rate_limit.rs` | 业务预算内移；IP输入提取在外 | T01/T08 |
| `authorization-server/src/http/token/jwt_bearer.rs` | 343 | 混合package依赖/职责归属需切割 | `App/token/jwt_bearer.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/native_sso.rs` | 431 | 混合package依赖/职责归属需切割 | `App/token/native_sso.rs` | P7共享状态helper，P8剩余用例，唯一文件不复制 | T01/T07/T08 |
| `authorization-server/src/http/token/refresh.rs` | 374 | 混合package依赖/职责归属需切割 | `App/token/refresh.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token/token_exchange.rs` | 515 | 混合package依赖/职责归属需切割 | `App/token/token_exchange.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T08 |
| `authorization-server/src/http/token.rs` | 244 | 混合package依赖/职责归属需切割 | `App/token/mod.rs + Native/http/token.rs` | App声明grant服务；Native路由/提取/呈现 | T01/T07/T08 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |
