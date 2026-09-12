# T03 — Symbol / Interface 固定规格

## F4. 仅新增有真实边界的能力

```rust
// App ports/audit.rs
pub type AuditFuture<'a> = std::pin::Pin<Box<
    dyn std::future::Future<Output = anyhow::Result<()>> + Send + 'a>>;
pub trait SecurityAudit: Send + Sync {
    fn ensure_storage(&self) -> AuditFuture<'_>;
    fn record(&self, event: &str, fields: serde_json::Map<String, serde_json::Value>);
    fn record_required<'a>(&'a self, event: &'a str,
        fields: serde_json::Map<String, serde_json::Value>) -> AuditFuture<'a>;
}
// App ports/remote_request_object.rs
pub type RequestObjectFuture<'a> = std::pin::Pin<Box<
    dyn std::future::Future<Output = Result<String, String>> + Send + 'a>>;
pub trait RemoteRequestObjectResolverPort: Send + Sync {
    fn resolve_request_object<'a>(&'a self, uri: &'a str) -> RequestObjectFuture<'a>;
}
// App ports/mdoc.rs
pub trait MdocDocumentSigner: Send + Sync {
    fn sign<'a>(&'a self,
        builder: mdoc_rs::builder::DocumentBuilder,
        lease: nazo_key_management::Openid4vcSigningLease,
        certificate_der: Vec<u8>,
    ) -> nazo_digital_credentials::CredentialFuture<'a,
        Result<mdoc_rs::model::document::IssuerSignedDocument,
               nazo_digital_credentials::CredentialTrustError>>;
}
// key-management/src/external_signer.rs
pub struct ExternalSignRequest<'a> {
    pub kid: &'a str,
    pub algorithm: jsonwebtoken::Algorithm,
    pub key_ref: &'a str,
    pub signing_input: &'a [u8],
}
pub trait ExternalKeySigner: Send + Sync {
    fn sign<'a>(&'a self, request: ExternalSignRequest<'a>) -> std::pin::Pin<Box<
        dyn std::future::Future<Output = Result<nazo_auth::Signature,
            nazo_auth::SignError>> + Send + 'a>>;
}
```

RemoteJwks 与 SectorIdentifier 已有 Port，不能重复创建。SecurityAudit 绑定租户及同一 Native sink；不是 queue/spawn 抽象。mdoc 直接使用现有普通库 owned builder 和结果，不复制 namespace/CBOR DTO。既有 nazo_auth::Signer 并非可直接 dyn 化的对象安全 trait，不修改整个签名系统；ExternalKeySigner 只表达外部密钥能力。

## F5. 后台单批操作与调度

```rust
pub trait CibaPingSender: Send + Sync {
    fn send<'a>(&'a self, delivery: &'a CibaPingDelivery)
        -> std::pin::Pin<Box<dyn std::future::Future<
            Output = anyhow::Result<http::StatusCode>> + Send + 'a>>;
}
pub trait BackchannelLogoutSender: Send + Sync {
    fn send<'a>(&'a self, delivery: &'a nazo_auth::BackchannelLogoutDelivery)
        -> std::pin::Pin<Box<dyn std::future::Future<
            Output = anyhow::Result<http::StatusCode>> + Send + 'a>>;
}
impl CibaPingDeliveryWorker {
    pub async fn process_due_batch(&self) -> anyhow::Result<usize>;
}
impl BackchannelLogoutWorker {
    pub async fn process_due_batch(&self) -> anyhow::Result<usize>;
}
```

Worker 构造器固定接既有 store Arc + 对应 sender Arc，删除 reqwest client/runtime 配置。CIBA item 使用迁入 App ports/transient_state.rs 的原 CibaPingDelivery，Logout item 使用 nazo_auth::BackchannelLogoutDelivery，不新建队列消息模型。批内 buffer_unordered 保留已有预算；claim/finish/retry 在 App。Native job 持 JoinHandle、sleep 和 abort/await；Native sender 负责 DNS/HTTP/deadline，并返回 HTTP status，不决定业务重试。

KeyManager::refresh 原签名保留；run_lifecycle/stop_lifecycle 从 key crate 删除。Native KeyLifecycleTask 持 watch Sender+JoinHandle；stop(self).await 只打断等待，不取消正在执行的 refresh。不得造 Runtime/Executor/AsyncRuntime/Platform 接口。

## F12. 构造器、launchers 与已有 Adapter

PG的PostgresProvider及new(DbPool)公开；原 provider实现不改。PostgresLauncher、PostgresOperatorPersistence与仅被其使用的常量移 Native launchers/postgres.rs；OperatorPersistence trait跟随operator模块留Native。

Valkey原providers保持private，增加 `pub fn server_state_bindings(client:nazo_valkey::ValkeyClient)->ServerStateBackendBindings`，只提取原工厂最后构造表达式；Native负责connect/config。不得重建key/schema/CAS。

Object Store的LocalAvatarObjectStoreProvider、S3AvatarObjectStoreProvider、TenantStorageConfig/Provider与launcher config选型移Native。S3AvatarObjectStore及实际AvatarDirectUploadPort实现保留原Adapter。原validate_config变成S3AvatarObjectStoreConfig::validate()，原构造器与Native调用唯一校验实现，不复制。

Native main明确导入自身三个launcher，保持命令和二进制名。删除旧 nazo_oauth_server::cli/config/operator_task/bootstrap public surface；不能用re-export维护旧内部路径。
