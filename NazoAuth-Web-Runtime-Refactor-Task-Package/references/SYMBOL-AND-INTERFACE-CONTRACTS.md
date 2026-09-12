# 固定接口与 Symbol Ownership

## F1. 中立契约唯一 owner

下表各 Symbol 保留原名、字段、derive、默认方法与 future 的 Send/!Send；移动其定义和 impl，所有消费者明确改 import。表中 http-actix 源路径在后续附录展开到行号。

| Symbol | 当前 | 唯一目标 | 修改原因/方式 | Phase |
|---|---|---|---|---|
| `AuthorizationDecisionFuture` | `http-actix/src/authorization_decision.rs:17` | `authorization-server/src/contracts/authorization_decision.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AuthorizationDecisionCommand` | `http-actix/src/authorization_decision.rs:26` | `authorization-server/src/contracts/authorization_decision.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AuthorizationDecisionResponse` | `http-actix/src/authorization_decision.rs:34` | `authorization-server/src/contracts/authorization_decision.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AuthorizationDecisionError` | `http-actix/src/authorization_decision.rs:47` | `authorization-server/src/contracts/authorization_decision.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AuthorizationDecisionOperations` | `http-actix/src/authorization_decision.rs:60` | `authorization-server/src/contracts/authorization_decision.rs` | 移动定义/impl；删除旧导出 | T02 |
| `LocalRegistrationFuture` | `http-actix/src/local_registration.rs:20` | `authorization-server/src/contracts/local_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `LocalRegistrationOperations` | `http-actix/src/local_registration.rs:22` | `authorization-server/src/contracts/local_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AuthenticationRateLimitError` | `http-actix/src/local_registration.rs:36` | `authorization-server/src/contracts/local_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AuthenticationRateLimit` | `http-actix/src/local_registration.rs:41` | `authorization-server/src/contracts/local_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasswordLoginFuture` | `http-actix/src/password_login.rs:22` | `authorization-server/src/contracts/password_login.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasswordLoginOperations` | `http-actix/src/password_login.rs:26` | `authorization-server/src/contracts/password_login.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyFuture` | `http-actix/src/passkey.rs:25` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyEndpointError` | `http-actix/src/passkey.rs:29` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyLoginFinishCommand` | `http-actix/src/passkey.rs:41` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyLoginOperations` | `http-actix/src/passkey.rs:50` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyProfileContext` | `http-actix/src/passkey.rs:57` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyRegistrationFinishCommand` | `http-actix/src/passkey.rs:62` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PasskeyProfileOperations` | `http-actix/src/passkey.rs:68` | `authorization-server/src/contracts/passkey.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaProfileFuture` | `http-actix/src/mfa_profile.rs:19` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaRequestContext` | `http-actix/src/mfa_profile.rs:23` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaCodeCommand` | `http-actix/src/mfa_profile.rs:31` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaChallengeCommand` | `http-actix/src/mfa_profile.rs:37` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaSessionRotation` | `http-actix/src/mfa_profile.rs:44` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaTotpEnrollment` | `http-actix/src/mfa_profile.rs:50` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaTotpConfirmation` | `http-actix/src/mfa_profile.rs:56` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaChallengeSuccess` | `http-actix/src/mfa_profile.rs:62` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaStepUpSuccess` | `http-actix/src/mfa_profile.rs:69` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaBackupCodesRegenerated` | `http-actix/src/mfa_profile.rs:75` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaProfileErrorKind` | `http-actix/src/mfa_profile.rs:81` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaProfileError` | `http-actix/src/mfa_profile.rs:100` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MfaProfileOperations` | `http-actix/src/mfa_profile.rs:136` | `authorization-server/src/contracts/mfa_profile.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ProfileAccountFuture` | `http-actix/src/profile_account.rs:18` | `authorization-server/src/contracts/profile_account.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ProfileMe` | `http-actix/src/profile_account.rs:22` | `authorization-server/src/contracts/profile_account.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ProfileAccountError` | `http-actix/src/profile_account.rs:28` | `authorization-server/src/contracts/profile_account.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ProfileAccountOperations` | `http-actix/src/profile_account.rs:38` | `authorization-server/src/contracts/profile_account.rs` | 移动定义/impl；删除旧导出 | T02 |
| `OidcLogoutFuture` | `http-actix/src/oidc_logout.rs:16` | `authorization-server/src/contracts/oidc_logout.rs` | 移动定义/impl；删除旧导出 | T02 |
| `OidcLogoutRequest` | `http-actix/src/oidc_logout.rs:20` | `authorization-server/src/contracts/oidc_logout.rs` | 移动定义/impl；删除旧导出 | T02 |
| `OidcLogoutCommand` | `http-actix/src/oidc_logout.rs:28` | `authorization-server/src/contracts/oidc_logout.rs` | 移动定义/impl；删除旧导出 | T02 |
| `OidcLogoutSuccess` | `http-actix/src/oidc_logout.rs:36` | `authorization-server/src/contracts/oidc_logout.rs` | 移动定义/impl；删除旧导出 | T02 |
| `OidcLogoutError` | `http-actix/src/oidc_logout.rs:42` | `authorization-server/src/contracts/oidc_logout.rs` | 移动定义/impl；删除旧导出 | T02 |
| `OidcLogoutOperations` | `http-actix/src/oidc_logout.rs:59` | `authorization-server/src/contracts/oidc_logout.rs` | 移动定义/impl；删除旧导出 | T02 |
| `SessionManagementFuture` | `http-actix/src/session_management.rs:14` | `authorization-server/src/contracts/session_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `SessionManagementOriginFuture` | `http-actix/src/session_management.rs:16` | `authorization-server/src/contracts/session_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `SessionManagementAvailability` | `http-actix/src/session_management.rs:20` | `authorization-server/src/contracts/session_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `SessionManagementError` | `http-actix/src/session_management.rs:33` | `authorization-server/src/contracts/session_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `SessionManagementOperations` | `http-actix/src/session_management.rs:38` | `authorization-server/src/contracts/session_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MetadataEndpointConfig` | `http-actix/src/metadata.rs:14` | `authorization-server/src/contracts/metadata.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MetadataSnapshot` | `http-actix/src/metadata.rs:28` | `authorization-server/src/contracts/metadata.rs` | 移动定义/impl；删除旧导出 | T02 |
| `MetadataSnapshotSource` | `http-actix/src/metadata.rs:37` | `authorization-server/src/contracts/metadata.rs` | 移动定义/impl；删除旧导出 | T02 |
| `RuntimeModuleAdminFuture` | `http-actix/src/runtime_modules.rs:32` | `authorization-server/src/contracts/runtime_modules.rs` | 移动定义/impl；删除旧导出 | T02 |
| `RuntimeModuleAdminError` | `http-actix/src/runtime_modules.rs:36` | `authorization-server/src/contracts/runtime_modules.rs` | 移动定义/impl；删除旧导出 | T02 |
| `RuntimeModuleAdministration` | `http-actix/src/runtime_modules.rs:43` | `authorization-server/src/contracts/runtime_modules.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ScimFuture` | `http-actix/src/scim.rs:30` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `ScimAuthorizedRequest` | `http-actix/src/scim.rs:33` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `ScimAuthorizationError` | `http-actix/src/scim.rs:40` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `ScimRequestAuthorizer` | `http-actix/src/scim.rs:50` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `ScimDependencyError` | `http-actix/src/scim.rs:67` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `ScimCursorProtector` | `http-actix/src/scim.rs:71` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `ScimBootstrapPasswordProvider` | `http-actix/src/scim.rs:76` | `authorization-server/src/contracts/scim.rs` | 移动定义/impl；删除旧导出 | T06 |
| `UserinfoFuture` | `http-actix/src/userinfo.rs:15` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T06 |
| `UserinfoRepresentation` | `http-actix/src/userinfo.rs:19` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T06 |
| `UserinfoSuccess` | `http-actix/src/userinfo.rs:25` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T06 |
| `UserinfoDpopError` | `http-actix/src/userinfo.rs:31` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T06 |
| `UserinfoError` | `http-actix/src/userinfo.rs:43` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T06 |
| `UserinfoOperations` | `http-actix/src/userinfo.rs:59` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T06 |
| `FapiFuture` | `http-actix/src/fapi_resource.rs:29` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `FapiAuthorizationError` | `http-actix/src/fapi_resource.rs:32` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `FapiResourceAuthorizer` | `http-actix/src/fapi_resource.rs:38` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `FapiSignatureVerificationError` | `http-actix/src/fapi_resource.rs:51` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `FapiSignatureOperationError` | `http-actix/src/fapi_resource.rs:59` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `FapiResponseSignature` | `http-actix/src/fapi_resource.rs:63` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `FapiHttpMessageSignatures` | `http-actix/src/fapi_resource.rs:72` | `authorization-server/src/contracts/fapi_resource.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TOKEN_INTROSPECTION_JWT_MEDIA_TYPE` | `http-actix/src/token_management.rs:18` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementFuture` | `http-actix/src/token_management.rs:20` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementRateLimitError` | `http-actix/src/token_management.rs:24` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementError` | `http-actix/src/token_management.rs:30` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenIntrospectionRepresentation` | `http-actix/src/token_management.rs:43` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementRequestFacts` | `http-actix/src/token_management.rs:52` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementRequestGuard` | `http-actix/src/token_management.rs:69` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementOperations` | `http-actix/src/token_management.rs:76` | `authorization-server/src/contracts/token_management.rs` | 移动定义/impl；删除旧导出 | T02 |
| `RemoteJwksFuture` | `http-actix/src/dynamic_client_registration/types.rs:11` | `authorization-server/src/contracts/dynamic_client_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `RemoteJwksResolverPort` | `http-actix/src/dynamic_client_registration/types.rs:14` | `authorization-server/src/contracts/dynamic_client_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `DynamicRegistrationRateLimitError` | `http-actix/src/dynamic_client_registration/types.rs:19` | `authorization-server/src/contracts/dynamic_client_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `DynamicRegistrationRequestGuard` | `http-actix/src/dynamic_client_registration/types.rs:24` | `authorization-server/src/contracts/dynamic_client_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `DynamicRegistrationSecurityServices` | `http-actix/src/dynamic_client_registration/types.rs:52` | `authorization-server/src/contracts/dynamic_client_registration.rs` | 移动定义/impl；删除旧导出 | T02 |
| `AccessTokenAuthScheme` | `http-actix/src/extract.rs:40` | `authorization-server/src/contracts/userinfo.rs` | 移动定义/impl；删除旧导出 | T02 |
| `DpopErrorContext` | `http-actix/src/dpop.rs:13` | `authorization-server/src/contracts/request_facts.rs` | 移动定义/impl；删除旧导出 | T02 |
| `BasicAuthorizationCredentials` | `http-actix/src/token_client_auth.rs:6` | `authorization-server/src/contracts/token_client_auth.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ClientCertificateFacts` | `http-actix/src/token_client_auth.rs:37` | `authorization-server/src/contracts/token_client_auth.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenClientAuthTransportFacts` | `http-actix/src/token_client_auth.rs:54` | `authorization-server/src/contracts/token_client_auth.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenForm` | `http-actix/src/token_forms.rs:12` | `authorization-server/src/contracts/token_forms.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenOnlyForm` | `http-actix/src/token_forms.rs:36` | `authorization-server/src/contracts/token_forms.rs` | 移动定义/impl；删除旧导出 | T02 |
| `PreAuthorizedTokenParameters` | `http-actix/src/token_forms.rs:45` | `authorization-server/src/contracts/token_forms.rs` | 移动定义/impl；删除旧导出 | T02 |
| `ParsedTokenForm` | `http-actix/src/token_forms.rs:51` | `authorization-server/src/contracts/token_forms.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenFormError` | `http-actix/src/token_forms.rs:57` | `authorization-server/src/contracts/token_forms.rs` | 移动定义/impl；删除旧导出 | T02 |
| `TokenManagementFormError` | `http-actix/src/token_forms.rs:66` | `authorization-server/src/contracts/token_forms.rs` | 移动定义/impl；删除旧导出 | T02 |
| `CredentialIssuerFuture` | `openid4vc-http-actix/src/vci.rs:12` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `AccessTokenScheme` | `openid4vc-http-actix/src/vci.rs:16` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CredentialRequestContext` | `openid4vc-http-actix/src/vci.rs:22` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CredentialResponseBody` | `openid4vc-http-actix/src/vci.rs:35` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CredentialEndpointResponse` | `openid4vc-http-actix/src/vci.rs:41` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CredentialRequestBody` | `openid4vc-http-actix/src/vci.rs:47` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PreAuthorizedTokenRequest` | `openid4vc-http-actix/src/vci.rs:53` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PreAuthorizedTokenResponse` | `openid4vc-http-actix/src/vci.rs:64` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CreateCredentialOfferRequest` | `openid4vc-http-actix/src/vci.rs:74` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CreateCredentialOfferResponse` | `openid4vc-http-actix/src/vci.rs:89` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CredentialHttpError` | `openid4vc-http-actix/src/vci.rs:96` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CredentialIssuerOperations` | `openid4vc-http-actix/src/vci.rs:103` | `openid4vci/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PresentationFuture` | `openid4vc-http-actix/src/vp.rs:9` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PresentationResponseBody` | `openid4vc-http-actix/src/vp.rs:12` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PresentationResponseInput` | `openid4vc-http-actix/src/vp.rs:18` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PresentationHttpError` | `openid4vc-http-actix/src/vp.rs:24` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CreatePresentationRequest` | `openid4vc-http-actix/src/vp.rs:32` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `CreatePresentationResponse` | `openid4vc-http-actix/src/vp.rs:56` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |
| `PresentationOperations` | `openid4vc-http-actix/src/vp.rs:64` | `openid4vp/src/application.rs` | 移动定义/impl；error.status 保留 u16 | T02 |

**不迁移的 HTTP 定义：**全部 Endpoint、MetadataHandles、SessionCookieConfig、OidcLogoutConfig、MfaProfileConfig、PasskeyLoginConfig、PasskeyProfileConfig、PasswordLoginConfig、SessionManagementConfig、未在表中列出的 HTTP 表单、ClientIpConfig / ClientIpHeaderMode / IpCidr、TokenManagementRequestFactsExtractor、VC ClientCertificateExtractor、ResourceAccessToken。TokenClientAuthForm 是提取器配合使用的借用视图，留在 Adapter。

删除无实际消费者的 `http-actix/src/request_context.rs::RequestContext`、module 与根导出。不要将它迁成 GenericRequest。

---

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

---

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

---

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

---

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

---

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

---

## F7. UserInfo 两阶段操作

只有 decode、audience、tenant、revocation 验证完成且 Bearer 的 cnf.x5t#S256 需要校验时，基线才提取 mTLS。固定保留这一顺序：

```rust
pub struct PreparedUserinfo {
    // 只有 owning App crate 能创建；字段 pub(crate)，外层不可伪造。
    pub(crate) scheme: AccessTokenAuthScheme,
    pub(crate) token: String,
    pub(crate) claims: nazo_auth::Claims,
}
impl PreparedUserinfo {
    pub fn requires_mtls_certificate(&self) -> bool;
}
pub struct UserinfoRequestFacts<'a> {
    pub dpop: DpopRequestFacts<'a>,
    pub mtls_thumbprint: Option<String>,
}
pub type UserinfoPreparationFuture<'a> = std::pin::Pin<Box<
    dyn std::future::Future<Output = Result<PreparedUserinfo, UserinfoError>> + 'a>>;
pub trait UserinfoOperations: Send + Sync {
    fn prepare<'a>(&'a self, scheme: AccessTokenAuthScheme, token: String)
        -> UserinfoPreparationFuture<'a>;
    fn userinfo<'a>(&'a self, prepared: PreparedUserinfo, facts: UserinfoRequestFacts<'a>)
        -> UserinfoFuture<'a>;
}
```

prepare 从原 userinfo 操作起始拆出到 revocation 后，保留错误顺序；第二段消费同一个 PreparedUserinfo，继续 sender-binding/claims/JWE，不再次 decode 或查撤销。requires_mtls_certificate 精确复用原“Bearer + x5t binding”分支判断，不把 DPoP scheme 的混合证书分支提前处理。

原 `FapiMtlsThumbprintResolver` 改名移到 `http-actix/src/mtls.rs::MtlsThumbprintExtractor`，保持 `resolve(&HttpRequest)->Option<String>`，明确只是 Adapter 内提取契约。Native 实现改 ServerMtlsThumbprintExtractor，放 Native http/mtls.rs。FAPI 与 UserInfo 复用；它不进入 App。UserinfoEndpoint.prepare 成功后才按需调用；DPoP header 的读取不得提前报错。

---

## F8. Authorization / PAR / JAR / JARM

App `authorization/` 承载原 protocol orchestration；Native `http/authorization/` 仅 parser、routing、CSRF、presentation。

固定输入分开：AuthorizationRequestFacts 保存 source_ip、session_id（可选）、user_agent（可选）；ParRequestFacts 保存 source_ip、TokenClientAuthTransportFacts、ClientAuthRequestFacts、DpopRequestFacts。参数使用原解析结果与重复 resource 表示，不能改成丢失重复值的简单 map。Authorization 与 PAR 不带 token idempotency/pre-authorized 字段。

AuthorizationApplication 提供 authorize、par、consent、client_presentation；其内部句柄都使用 App services/ports/config/snapshot/audit，不接 HTTP request。AuthorizationOutcome 直接使用同 owning crate 已有 AuthorizationDecisionResponse（允许本 owner 语义 type alias），保留其 Redirect/FormPost 等既有字段；无须 GenericResponse。

GET/POST authorize 的 Redirect302 与 decision303 在原 Adapter 调用位置保留。App 提供 action、参数、session_state、CSP nonce；HTML escaping、CSP/Content-Type、form_post document 属 Adapter。PAR201继续原 json_response_status 的 header/cache 行为，不将所有成功统一 no-store。

JAR error 在 App typed error 上判断是否允许 redirect，不能先变 HttpResponse 再读 extension。注册 client/redirect URI 校验前禁止重定向。PAR rate limit 保持 parser之前；mTLS提取保持 PAR 原调用位置，不抄 token 的先后顺序。

ClientPresentation 固定字段 client_name:String、logo_uri/policy_uri/tos_uri:Option<String>；错误 NotFound/Unavailable。Native client_id query 必须恰好一个、≤255字节、VSCHAR(0x21..=0x7e)，400/404/503保持只包含 error 的原 JSON，不添加 description。consent 接 session_id/request_id 原顺序校验，返回原 ConsentPayload；Native 仅增加 csrf_token，不删除 request_id、client_id、client_name、redirect_uri、scopes、userinfo_claims、id_token_claims、authorization_details。

---

## F9. 动态客户端注册不是只移动 trait

唯一 `domain/dynamic_registration.rs::DynamicRegistrationApplication` 持原 config、clients、sector_identifiers、security、request_guard。使用原 DynamicRegistrationRequestGuard；不为唯一实现再造 Operations trait。

create/read/update/delete 的完整 store/crypto/policy/audit 编排从 `http-actix/src/dynamic_client_registration/handlers.rs` 迁入 App；auth.rs 中不依赖 HTTP 的 token验证随迁。参数分别为原 typed body、client_id、Authorization 第一项有效文本、source_ip。body解析、IP提取、header grammar、response mapping留 Adapter；read/delete不引入不存在的JSON body。

结果分为 Created、Read、Updated、Deleted；Created/Updated包含各自原完整response body构造数据，Read保留当前 registration token。不能把 PUT 误改为“不旋转 token”。合并原 domain config 与 DynamicRegistrationEndpointConfig 的业务字段到一个 App config；proxy/IP字段仍留Endpoint。POST/PUT的admission在JSON提取前、JSON提取在限流前；GET/DELETE原顺序不变。

业务实现不再构造 Endpoint；Native `bootstrap/startup/services/dependencies.rs` 构造 Application及Endpoint。ServerDynamicRegistrationTokens/RequestGuard归 App，依赖纯crypto/snapshot/audit/原Port；具体RemoteClientDocumentResolver留Native。

---

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

---

## F11. CIBA / Device 的创建和决定

App PreparedCibaCreation 仅保存原 BackchannelAuthenticationForm；PreparedDeviceAuthorization 保存原 DeviceAuthorizationForm + has_basic。字段private，只公开 form()借用访问。prepare_* 使用原认证方式冲突和client_id/hint规则，必须先于昂贵证书提取。

CibaCreationResponse 为 auth_req_id/expires_in/interval；DeviceAuthorizationResponse 为 device_code/user_code/verification_uri/verification_uri_complete/expires_in/interval，整数宽度与原数据保持。DeviceVerificationData 为 user_code + 原 Option<DeviceAuthorizationPayload>；不因分层新增登录要求。

CibaApplication 持 authorization、CibaTokenHandles、RemoteJwksResolverPort、SnapshotStore、SecurityAudit。DeviceDecisionHandles 持原 authorization/device service/grant_repository/config/snapshot/remote_jwks/limiter/audit；sessions HTTP handle 删除。固定操作：check_admission、create、verification、decide；Device另有 enforce_creation_rate_limit。create收 prepared、认证事实、ClientAuthRequestFacts、source_ip；decide收原请求id或user_code、decision、CurrentSession、source_ip。

admission 在原 handler守卫位置只读一次，不在 create 重读快照。HTTP CIBA decide固定 expected_user_id=Some(session.user.id())，禁止外层传None绕过。CSRF/cookies/JSON/HTML在Native；已有事务、审计intent→decision→结果审计顺序在App。

---

## F12. 构造器、launchers 与已有 Adapter

PG的PostgresProvider及new(DbPool)公开；原 provider实现不改。PostgresLauncher、PostgresOperatorPersistence与仅被其使用的常量移 Native launchers/postgres.rs；OperatorPersistence trait跟随operator模块留Native。

Valkey原providers保持private，增加 `pub fn server_state_bindings(client:nazo_valkey::ValkeyClient)->ServerStateBackendBindings`，只提取原工厂最后构造表达式；Native负责connect/config。不得重建key/schema/CAS。

Object Store的LocalAvatarObjectStoreProvider、S3AvatarObjectStoreProvider、TenantStorageConfig/Provider与launcher config选型移Native。S3AvatarObjectStore及实际AvatarDirectUploadPort实现保留原Adapter。原validate_config变成S3AvatarObjectStoreConfig::validate()，原构造器与Native调用唯一校验实现，不复制。

Native main明确导入自身三个launcher，保持命令和二进制名。删除旧 nazo_oauth_server::cli/config/operator_task/bootstrap public surface；不能用re-export维护旧内部路径。