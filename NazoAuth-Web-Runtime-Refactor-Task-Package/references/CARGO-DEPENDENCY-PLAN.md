# H. Cargo Dependency 变化

| Manifest | 删除/移动 | 新增/保留 | 必要性 |
|---|---|---|---|
| 根Cargo.toml | workspace members不增；版本/patch/release配置不变 | workspace http="1.4.2"；复用现有futures-executor | HTTP标准类型已经由resource-server使用 |
| authorization-server/Cargo.toml | 删除actix-*、tokio、reqwest、SMTP、OTel导出/安装、filesystem/process配置库、nazo-http-actix、VC Actix、operator-protocol、Native缓存/execution依赖 | 保留实际用到的domain packages、std/futures、serde/json/chrono/url/uuid/crypto；新增http | App无具体Web/Runtime/Host正常依赖 |
| nazoauth/Cargo.toml | 不改bin名称/path/test=false | 接收原server具体依赖及原features；增加http/process-wrap；nazo-postgres/nazo-valkey为normal依赖 | 启动器移入现有Host |
| http-actix/Cargo.toml | 不依赖Native或存储Adapter | 新增nazo-oauth-server.workspace/http.workspace；保留transport库 | Adapter向内消费唯一contract |
| openid4vc-http-actix/Cargo.toml | 不增加App dependency | 原VCI/VP依赖，改module import | 各协议拥有契约 |
| openid4vci、openid4vp Cargo.toml | 不加Actix/Tokio正常依赖 | 只补迁入定义真正使用的现有workspace库 | 不新增共享contracts crate |
| key-management/Cargo.toml | 删除normal tokio/process-wrap；进程测试随迁 | external_signer仅std/Core；纯async tests可用futures-executor dev | key只描述语义 |
| authorization-server-postgres/Cargo.toml | 移走launcher/operator专用依赖，含仅它们用的anyhow | 保留App ports、nazo-postgres及真实domain依赖 | 不依赖Host |
| authorization-server-valkey/Cargo.toml | 移走launcher/config专用依赖与anyhow | 保留App ports/nazo-valkey | 同上 |
| authorization-server-object-store/Cargo.toml | 移走launcher/config依赖；删除anyhow与nazo-oauth-server（其用途随Native provider迁出） | 保留identity/S3实际实现依赖 | 已有存储能力不重做 |
| runtime-capabilities、identity Cargo.toml | 不变 | 不变 | accessor/Arc impl无需新库 |

server移Native的具体依赖清单包括：actix-cors/files/multipart/web/tls、tokio、reqwest、lettre SMTP执行、opentelemetry/sdk/otlp、tracing-opentelemetry/subscriber、atomicwrites、fs2、rustix、tar、flate2、yaml_serde、semver、lru、futures-channel、arc-swap中仅Native调度/缓存用途、Argon2执行、ed25519-dalek/rcgen/sha1/time/yasna/zeroize中原Native配置与证书生成用途。**库在App纯业务仍真实使用时保留该必要依赖**，不得把“移某用途”误读为盲删全部；例如已有crypto.rs的der/x509-cert/AWS-LC保留，passkey-auth因中立AuthenticationResponse/RegistrationResponse继续保留，rustls/webpki的纯证书链验证可保留但连接类型不可进入。

旧server的diesel/diesel-async/diesel_migrations/nazo-postgres/nazo-valkey/fred dev依赖随IO测试迁Native；App fake tests不反向dev-depend Native。pkcs8/proptest/key-management test-support留真实使用方。

基线约束与lock区别：Actix manifest4.14.0，lock实际4.15.0；http存在0.2.12与1.5.0。Actix http类型不等于http1类型。只在Adapter用Method::from_bytes、Uri解析、StatusCode::from_u16转换；不复制全部headers，不为类型冲突降级全项目http。reqwest现有0.12.28 dev与0.13.4 normal不在本任务统一。

每个真正改变manifest的原子Step：先一次**不带--locked的定向cargo check**同步workspace dependency list，再检查Cargo.lock；允许workspace包依赖清单变更，不允许registry/git版本/source/checksum漂移。随后所有验证用--locked。禁止cargo update、升级工具链、mdoc/Actix依赖。普通Step不重复解锁。