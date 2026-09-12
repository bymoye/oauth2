# T08 — Symbol / Interface 固定规格

## F2. 业务专用 Request Facts

以下代码为固定接口草案。已存在的类型按 F1 移动；不另造同名简化模型。借用 proof 避免复制大 JWT；错误保留到原业务校验位置，不能 ingress 统一提前失败。

```rust
// contracts/request_facts.rs
pub struct DpopRequestFacts<'a> {
    pub method: http::Method,
    pub path: &'a str,
    pub proof: Result<Option<&'a str>, nazo_auth::DpopError>,
    pub proof_present: bool,
}
// contracts/scim.rs
pub struct ScimAuthenticationFacts<'a> {
    pub bearer_token: Option<&'a str>,
    pub source_ip: String,
    pub user_agent: Option<&'a str>,
}
// ScimRequestAuthorizer：原 future 输出和约束不变，只替换 request 输入。
fn authorize<'a>(
    &'a self,
    facts: ScimAuthenticationFacts<'a>,
    required_scope: nazo_identity::scim::ScimRequiredScope,
) -> ScimFuture<'a, Result<ScimAuthorizedRequest, ScimAuthorizationError>>;

// contracts/token_endpoint.rs
pub struct ClientAttestationFacts<'a> {
    pub any_header_present: bool,
    pub strict_pair: Result<Option<(&'a str, &'a str)>, ()>,
    pub first_attestation: Option<&'a str>,
    pub first_pop: Option<&'a str>,
}
pub struct TokenRequestFacts<'a> {
    pub dpop: DpopRequestFacts<'a>,
    pub first_dpop_header: Option<&'a str>,
    pub client_attestation: ClientAttestationFacts<'a>,
    pub certificate: Option<ClientCertificateFacts>,
    pub request_target: http::Uri,
    pub idempotency_key: Option<String>,
}
```

TokenClientAuthTransportFacts 独立保存客户端认证材料，不塞进 TokenRequestFacts。增加唯一构造器：

```rust
pub fn from_parts(
    basic: BasicAuthorizationCredentials,
    client_id: Option<String>, client_secret: Option<String>,
    client_assertion_type: Option<String>, client_assertion: Option<String>,
) -> TokenClientAuthTransportFacts;
```

其字段继续 private、Debug 继续脱敏；Basic 枚举仅扩大可见性。ClientCertificateFacts 直接迁原字段：thumbprint、subject_dn、san_dns、san_uri、san_ip、san_email、verified_certificate_expiry、certificate_chain_der、deployment_trusted_chain。只需要 binding 的入口收 thumbprint；真正执行 PKI client auth 才收完整证书事实。

TokenManagementRequestFacts 已有 source_ip、endpoint_path、client_certificate，原样复用。FAPI 原有 ProtectedResource 请求/上下文原样复用；VC 已有 CredentialRequestContext 原样复用，不为统一把所有 URL 和 method 换模型。

DPoP 的 htu 继续由可信 issuer/mTLS issuer 与 path 生成，不能使用 Host/Forwarded 拼“外部 URL”。pre-authorized 的 request_url 保留 issuer + 原 req.uri()（包括 query）；普通 DPoP path 不含 query。FAPI 签名保留其独立 method/target URI/body/header capture，不能为全项目统一 URL 而改变其基串。

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
