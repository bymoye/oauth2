# T10 — Symbol / Interface 固定规格

## F11. CIBA / Device 的创建和决定

App PreparedCibaCreation 仅保存原 BackchannelAuthenticationForm；PreparedDeviceAuthorization 保存原 DeviceAuthorizationForm + has_basic。字段private，只公开 form()借用访问。prepare_* 使用原认证方式冲突和client_id/hint规则，必须先于昂贵证书提取。

CibaCreationResponse 为 auth_req_id/expires_in/interval；DeviceAuthorizationResponse 为 device_code/user_code/verification_uri/verification_uri_complete/expires_in/interval，整数宽度与原数据保持。DeviceVerificationData 为 user_code + 原 Option<DeviceAuthorizationPayload>；不因分层新增登录要求。

CibaApplication 持 authorization、CibaTokenHandles、RemoteJwksResolverPort、SnapshotStore、SecurityAudit。DeviceDecisionHandles 持原 authorization/device service/grant_repository/config/snapshot/remote_jwks/limiter/audit；sessions HTTP handle 删除。固定操作：check_admission、create、verification、decide；Device另有 enforce_creation_rate_limit。create收 prepared、认证事实、ClientAuthRequestFacts、source_ip；decide收原请求id或user_code、decision、CurrentSession、source_ip。

admission 在原 handler守卫位置只读一次，不在 create 重读快照。HTTP CIBA decide固定 expected_user_id=Some(session.user.id())，禁止外层传None绕过。CSRF/cookies/JSON/HTML在Native；已有事务、审计intent→decision→结果审计顺序在App。
