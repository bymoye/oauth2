# T06 — Symbol / Interface 固定规格

## Canonical Symbol 迁移

| Symbol | 当前 | 唯一目标 | 修改原因/方式 | Task |
|---|---|---|---|---|
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
