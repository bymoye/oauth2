# T11 — Symbol / Interface 固定规格

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
