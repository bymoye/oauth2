# T09 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/authorization_decision.rs` | 379 | 混合package依赖/职责归属需切割 | `App/domain/authorization_decision.rs` | 业务整体内移，原model/impl保留；改服务/契约imports | T01/T09 |
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
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
| `authorization-server/src/http/views.rs` | 225 | 混合package依赖/职责归属需切割 | `App/authorization/presentation.rs + Native/http/views.rs` | 仅append_query纯helper内移；HTML在外 | T01/T09 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |

## E2. HTTP Adapter全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `http-actix/src/lib.rs` | `原文件` | 模块/导出更新，删除旧contract兼容surface | T02/T05/T06/T09 |
| `http-actix/src/presenter.rs` | `原文件` | 新增typed错误presenter；P9删OAuthJsonErrorFields | T07/T09 |
