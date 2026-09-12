# T12 — Symbol / Interface 固定规格

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
