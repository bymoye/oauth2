# T10 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/http/token/ciba/backchannel.rs` | 375 | 混合package依赖/职责归属需切割 | `App/token/ciba/backchannel.rs + Native/http/token/ciba/backchannel.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/decision.rs` | 350 | 混合package依赖/职责归属需切割 | `App/token/ciba/decision.rs + Native/http/token/ciba/decision.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/request.rs` | 428 | 混合package依赖/职责归属需切割 | `App/token/ciba/request.rs + Native/http/token/ciba/request.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba/state.rs` | 206 | 混合package依赖/职责归属需切割 | `App/token/ciba/state.rs + Native/http/token/ciba/state.rs` | 纯表单/政策/业务内移，wire parser/CSRF/呈现留Native | T01/T08/T10 |
| `authorization-server/src/http/token/ciba.rs` | 113 | 混合package依赖/职责归属需切割 | `App/token/ciba/mod.rs + Native/http/token/ciba.rs` | App业务父模块/Native路由父模块分开 | T01/T08/T10 |
| `authorization-server/src/http/token/device.rs` | 812 | 混合package依赖/职责归属需切割 | `App/token/device.rs + App/contracts/device.rs + Native/http/token/device.rs` | 业务与纯模型内移，parse/CSRF/HTTP保留 | T01/T10 |
| `authorization-server/src/http/token/device_config.rs` | 38 | 混合package依赖/职责归属需切割 | `App/token/device_config.rs + Native/http/token/device_config.rs` | DeviceConfig业务字段内移；HTTP字段在外 | T01/T10 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |
