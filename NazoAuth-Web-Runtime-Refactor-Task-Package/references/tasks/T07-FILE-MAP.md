# T07 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/http/token/ciba/policy.rs` | 179 | 混合package依赖/职责归属需切割 | `App/token/ciba/policy.rs` | token polling/policy内移，移除response/request | T01/T07/T08 |
| `authorization-server/src/http/token/ciba/poll.rs` | 418 | 混合package依赖/职责归属需切割 | `App/token/ciba/poll.rs` | token polling/policy内移，移除response/request | T01/T07/T08 |
| `authorization-server/src/http/token/dispatch/mod.rs` | 688 | 混合package依赖/职责归属需切割 | `App/token/dispatch/mod.rs + Native/http/token/dispatch/mod.rs` | App handles/execute；Native parse/facts/presenter | T01/T07/T08 |
| `authorization-server/src/http/token/issue/authorization_code_state.rs` | 78 | 混合package依赖/职责归属需切割 | `App/token/issue/authorization_code_state.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/issue/refresh_persistence.rs` | 98 | 混合package依赖/职责归属需切割 | `App/token/issue/refresh_persistence.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/issue.rs` | 406 | 混合package依赖/职责归属需切割 | `App/token/issue.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/issue_grant.rs` | 707 | 混合package依赖/职责归属需切割 | `App/token/issue_grant.rs` | 业务链整体内移，F3 typed结果与F2 facts | T01/T07 |
| `authorization-server/src/http/token/native_sso.rs` | 431 | 混合package依赖/职责归属需切割 | `App/token/native_sso.rs` | P7共享状态helper，P8剩余用例，唯一文件不复制 | T01/T07/T08 |
| `authorization-server/src/http/token.rs` | 244 | 混合package依赖/职责归属需切割 | `App/token/mod.rs + Native/http/token.rs` | App声明grant服务；Native路由/提取/呈现 | T01/T07/T08 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |

## E2. HTTP Adapter全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `http-actix/src/presenter.rs` | `原文件` | 新增typed错误presenter；P9删OAuthJsonErrorFields | T07/T09 |
