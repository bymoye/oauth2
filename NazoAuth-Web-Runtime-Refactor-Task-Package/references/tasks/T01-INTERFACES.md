# T01 — Symbol / Interface 固定规格

## F12. 构造器、launchers 与已有 Adapter

PG的PostgresProvider及new(DbPool)公开；原 provider实现不改。PostgresLauncher、PostgresOperatorPersistence与仅被其使用的常量移 Native launchers/postgres.rs；OperatorPersistence trait跟随operator模块留Native。

Valkey原providers保持private，增加 `pub fn server_state_bindings(client:nazo_valkey::ValkeyClient)->ServerStateBackendBindings`，只提取原工厂最后构造表达式；Native负责connect/config。不得重建key/schema/CAS。

Object Store的LocalAvatarObjectStoreProvider、S3AvatarObjectStoreProvider、TenantStorageConfig/Provider与launcher config选型移Native。S3AvatarObjectStore及实际AvatarDirectUploadPort实现保留原Adapter。原validate_config变成S3AvatarObjectStoreConfig::validate()，原构造器与Native调用唯一校验实现，不复制。

Native main明确导入自身三个launcher，保持命令和二进制名。删除旧 nazo_oauth_server::cli/config/operator_task/bootstrap public surface；不能用re-export维护旧内部路径。
