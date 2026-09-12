# T05 — Symbol / Interface 固定规格

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

## F9. 动态客户端注册不是只移动 trait

唯一 `domain/dynamic_registration.rs::DynamicRegistrationApplication` 持原 config、clients、sector_identifiers、security、request_guard。使用原 DynamicRegistrationRequestGuard；不为唯一实现再造 Operations trait。

create/read/update/delete 的完整 store/crypto/policy/audit 编排从 `http-actix/src/dynamic_client_registration/handlers.rs` 迁入 App；auth.rs 中不依赖 HTTP 的 token验证随迁。参数分别为原 typed body、client_id、Authorization 第一项有效文本、source_ip。body解析、IP提取、header grammar、response mapping留 Adapter；read/delete不引入不存在的JSON body。

结果分为 Created、Read、Updated、Deleted；Created/Updated包含各自原完整response body构造数据，Read保留当前 registration token。不能把 PUT 误改为“不旋转 token”。合并原 domain config 与 DynamicRegistrationEndpointConfig 的业务字段到一个 App config；proxy/IP字段仍留Endpoint。POST/PUT的admission在JSON提取前、JSON提取在限流前；GET/DELETE原顺序不变。

业务实现不再构造 Endpoint；Native `bootstrap/startup/services/dependencies.rs` 构造 Application及Endpoint。ServerDynamicRegistrationTokens/RequestGuard归 App，依赖纯crypto/snapshot/audit/原Port；具体RemoteClientDocumentResolver留Native。

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
