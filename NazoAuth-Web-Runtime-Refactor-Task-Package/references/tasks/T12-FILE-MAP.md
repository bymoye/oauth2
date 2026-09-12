# T12 — 文件迁移地图

仅包含本任务涉及的生产文件映射。若当前 HEAD 路径变化，按语义 owner 做最小映射，不改变目标职责。

## E1. authorization-server全部生产文件

| 源文件 | 行数 | 当前问题/判断 | 固定目标 | 操作 | Task |
|---|---:|---|---|---|---|
| `authorization-server/src/domain/backchannel_logout_worker.rs` | 280 | 混合package依赖/职责归属需切割 | `App/workers/backchannel_logout.rs + Native/adapters/backchannel_logout_sender.rs + Native/jobs/backchannel_logout.rs` | 同上；测试编译真实生产主体 | T01/T12 |
| `authorization-server/src/domain/ciba_ping_delivery.rs` | 203 | 混合package依赖/职责归属需切割 | `App/workers/ciba_ping.rs + Native/adapters/ciba_ping_sender.rs + Native/jobs/ciba_ping.rs` | 拆业务批次/具体发送/任务调度 | T01/T12 |
| `authorization-server/src/domain/ciba_ping_tls.rs` | 30 | 属于外层；原package同时承载业务 | `Native/adapters/ciba_ping_tls.rs` | 具体sender TLS装配整体外移 | T01/T12 |
| `authorization-server/src/domain/mod.rs` | 88 | 混合package依赖/职责归属需切割 | `App/domain/mod.rs` | 最终只声明业务子模块，删除Native domain父模块 | T01/T04–T12 |
| `authorization-server/src/lib.rs` | 34 | 混合package依赖/职责归属需切割 | `App/lib.rs + Native/lib.rs` | 拆根module：App声明中立模块，Native声明Host模块 | T01–T13 |
| `authorization-server/src/runtime_modules.rs` | 373 | 属于外层；原package同时承载业务 | `Native/runtime_modules.rs` | Native生命周期/registry装配；App使用共享SnapshotStore | T01/T04/T12 |
