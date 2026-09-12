# T09 — Symbol / Interface 固定规格

## F8. Authorization / PAR / JAR / JARM

App `authorization/` 承载原 protocol orchestration；Native `http/authorization/` 仅 parser、routing、CSRF、presentation。

固定输入分开：AuthorizationRequestFacts 保存 source_ip、session_id（可选）、user_agent（可选）；ParRequestFacts 保存 source_ip、TokenClientAuthTransportFacts、ClientAuthRequestFacts、DpopRequestFacts。参数使用原解析结果与重复 resource 表示，不能改成丢失重复值的简单 map。Authorization 与 PAR 不带 token idempotency/pre-authorized 字段。

AuthorizationApplication 提供 authorize、par、consent、client_presentation；其内部句柄都使用 App services/ports/config/snapshot/audit，不接 HTTP request。AuthorizationOutcome 直接使用同 owning crate 已有 AuthorizationDecisionResponse（允许本 owner 语义 type alias），保留其 Redirect/FormPost 等既有字段；无须 GenericResponse。

GET/POST authorize 的 Redirect302 与 decision303 在原 Adapter 调用位置保留。App 提供 action、参数、session_state、CSP nonce；HTML escaping、CSP/Content-Type、form_post document 属 Adapter。PAR201继续原 json_response_status 的 header/cache 行为，不将所有成功统一 no-store。

JAR error 在 App typed error 上判断是否允许 redirect，不能先变 HttpResponse 再读 extension。注册 client/redirect URI 校验前禁止重定向。PAR rate limit 保持 parser之前；mTLS提取保持 PAR 原调用位置，不抄 token 的先后顺序。

ClientPresentation 固定字段 client_name:String、logo_uri/policy_uri/tos_uri:Option<String>；错误 NotFound/Unavailable。Native client_id query 必须恰好一个、≤255字节、VSCHAR(0x21..=0x7e)，400/404/503保持只包含 error 的原 JSON，不添加 description。consent 接 session_id/request_id 原顺序校验，返回原 ConsentPayload；Native 仅增加 csrf_token，不删除 request_id、client_id、client_name、redirect_uri、scopes、userinfo_claims、id_token_claims、authorization_details。
