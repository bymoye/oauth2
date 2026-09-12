# T04 — Symbol / Interface 固定规格

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

## F6. 配置与会话

AuthorizationServerProfile、CibaSecurityProfile、RequestObjectJtiPolicy、SubjectType、Openid4vcRevocationPolicy 的 enum 与纯 predicate 移 App policy.rs。DpopNoncePolicy 直接复用 nazo_auth 定义。ConfigSource/env/default/PEM/path 加载留 Native settings；From<Settings> 改为 Native free factory，不能给另一个 crate 的类型写 inherent impl。

| 原模型 | App 字段 | Native/HTTP 字段 |
|---|---|---|
| AuthorizationHttpConfig→AuthorizationConfig | issuer/mTLS issuer/frontend/profile/nonce/JTI/TTL/PAR/pepper/阈值 | IP模式、CIDRs、Settings解析 |
| TokenIssuanceConfig | 原签发/scopes/audience/profile/TTL/VC字段 | proxy/IP提取 |
| ResourceServerConfig/UserinfoConfig | 原验证/nonce/signature policy | trusted_proxy_cidrs |
| CibaHttpConfig→CibaConfig | issuer/mTLS/frontend/pepper/audience/tenant/TTL/poll/profile | CIDRs/IP mode/CSRF cookie |
| DeviceHttpConfig→DeviceConfig | 原 device protocol/issuer/client policy | cookies/IP配置 |
| DynamicRegistrationConfig | tenant/issuer/audience/pairwise/pepper/initial token/算法与阈值 | proxy/IP/Endpoint构造 |
| KeySettings | rotation_interval/prepublish_window/verification_grace | external_command/external_timeout |

SessionResolver 字段固定为原 sessions:Arc<dyn SessionStorePort>、users:Arc<dyn SessionAccountPort>、tenant_id:TenantId。current_session_by_id/delete_session 原业务函数体移动；SessionPayload/CurrentSession 随迁。Native AdminSessionHandles/SessionProfileHandles 只持 Arc<SessionResolver> + SessionHttpConfig；cookie、CSRF、清cookie 与 HTTP错误仍外层。管理员/MFA policy 返回语义错误，不返回 response；用户的 amr/auth_time/oidc_sid 不丢失。

RuntimeModuleRegistry 新增 `pub fn snapshot_store(&self)->Arc<SnapshotStore>`，只 Arc::clone(&self.snapshots)。App 原每次 snapshot() 的地方改 load_full()；原每请求只固定一次的地方仍一次。不能另建 ModuleStatus Port 或复制快照。

## F10. 服务别名与构造闭包

```rust
// App services.rs：以下各 trait 来自 nazo_identity::ports。
pub type LocalAuthenticationService = nazo_identity::AuthenticationService<
    Arc<dyn LoginThrottlePort>, Arc<dyn SecretVerifyPort>,
    Arc<dyn LoginSessionPort>, Arc<dyn AuthenticationAuditPort>>;
pub type LocalRegistrationService = nazo_identity::RegistrationService<
    Arc<dyn EmailVerificationStorePort>, Arc<dyn SecretHashPort>,
    Arc<dyn VerificationEmailDeliveryPort>>;
pub type LocalPasskeyService = nazo_identity::PasskeyService<
    Arc<dyn PasskeyCeremonyPort>, Arc<dyn LoginSessionPort>, Arc<dyn PasskeyAuditPort>>;
pub type LocalFederationService = nazo_identity::FederationService<
    Arc<dyn FederationStatePort>, Arc<dyn FederationPasswordHasherPort>,
    Arc<dyn LoginSessionPort>, Arc<dyn FederationAuditPort>>;
```

只为七个尚无 Arc 转发的已有 Port 补 `impl<T: Port + ?Sized> Port for Arc<T>`：SecretVerifyPort、AuthenticationAuditPort；SecretHashPort、VerificationEmailDeliveryPort；PasskeyAuditPort；FederationPasswordHasherPort、FederationAuditPort。位于 identity ports/authentication.rs、registration.rs、passkey.rs、federation.rs。逐方法直接 `self.as_ref().method(args)`；不新增 wrapper、不重装 BoxFuture、不修改服务。

Native Tracing*Audit 改为持 Arc<dyn SecurityAudit> 的 Clone struct，删除 Copy；所有实例共享同一持久化sink。其他 ServerAuthorizationService、ServerTokenService、ServerCibaService、ServerDeviceGrantService 及纯profile aliases迁 services.rs。AvatarProfileService Disabled/Local/Direct保持Native，不把已有存储选择移入App。PasswordHashInput 使用已有 into_persistence_value()，不是臆造 as_str()。
