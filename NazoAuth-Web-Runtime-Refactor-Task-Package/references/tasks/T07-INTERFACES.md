# T07 — Symbol / Interface 固定规格

## F3. Token 预处理与结果模型

顺序固定：**source-IP 限流 → body parser → audience 参数约束 → auth-source 冲突检查 → 证书提取 → 其余认证/业务**。因此需要真正语义 preflight，而不是万能 ingress request。

```rust
pub struct PreparedTokenRequest {
    parsed: ParsedTokenForm,
    auth: TokenClientAuthTransportFacts,
}
pub fn prepare_token_request(
    parsed: ParsedTokenForm,
    auth: TokenClientAuthTransportFacts,
) -> Result<PreparedTokenRequest, OAuthEndpointError>;
impl TokenEndpointHandles {
    pub async fn execute(
        &self, prepared: PreparedTokenRequest, facts: TokenRequestFacts<'_>,
    ) -> Result<TokenEndpointSuccess, OAuthEndpointError>;
}
pub enum TokenEndpointSuccess {
    Issued { body: serde_json::Value, dpop_nonce: Option<String> },
    Replayed { body: Vec<u8> },
    PreAuthorized(nazo_openid4vci::application::PreAuthorizedTokenResponse),
}
```

PreparedTokenRequest 不保存新的 client_auth_context 类型；prepare 用现有纯函数检查，execute 用相同 auth.presentation() 重取廉价纯值。不得重复 IO、签名验证、assertion consume。业务句柄全部 Data→Arc；registry→同一 Arc<SnapshotStore>；remote resolver→Arc<dyn RemoteJwksResolverPort>。Openid4vcTokenHandles.credential_issuer 改 `Option<Arc<dyn nazo_openid4vci::application::CredentialIssuerOperations>>`，不能调用 HTTP Endpoint。

```rust
// contracts/oauth_error.rs
pub struct OAuthErrorFields {
    pub status: http::StatusCode,
    pub error: String,
    pub description: String,
}
pub enum OAuthEndpointError {
    Json(OAuthErrorFields),
    Authorization(OAuthErrorFields),
    Token { fields: OAuthErrorFields, basic_challenge: bool },
    Bearer(OAuthErrorFields),
    Dpop { error: nazo_auth::DpopError, context: DpopErrorContext },
    PreAuthorized(nazo_openid4vci::application::CredentialHttpError),
    RateLimited { retry_after_seconds: u64 },
    Disabled,
}
```

这是项目已有 OAuth 错误呈现语义，不是任意 response 容器。构造器 `json/authorization/token/bearer` 只填原字段；不携带任意 body/header/cookie。Adapter 新增 `presenter::oauth_endpoint_error_response` 调原 helper：Json→oauth_error；Authorization→原 authorization/ciba no-store；Token→oauth_token_error；Bearer→oauth_bearer_error；DPoP/VC 走原专用映射；Disabled→空404；RateLimited→原429+Retry-After。

原 ASCII error_description 限制不变：原中文描述在 presenter 被映成 `Request failed.` 的情况不能顺便“修复翻译”。T09 删除 OAuthJsonErrorFields 与 extension 读写，协议判断发生于呈现前。

Issued 保留 no-store + pragma + 可选 DPoP nonce；Replayed 必须输出原持久化 JSON bytes，只加原 Cache-Control/Content-Type，不增加 pragma、不重新生成 nonce；PreAuthorized 保留原 JSON+Cache-Control，不擅加 pragma。不能把三者归一化成 Value 后重新序列化。
