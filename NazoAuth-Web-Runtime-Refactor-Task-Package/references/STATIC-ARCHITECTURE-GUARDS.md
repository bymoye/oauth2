# I. 静态架构守卫

## I1. 复用 verify_static_contracts.py

增加简短PACKAGE_ROLES，覆盖D表21个package；角色只使用domain/application/adapter/host，contracts随owner。检查normal/build、本地路径、workspace别名、package重命名、optional及target-specific依赖：Domain→Domain；Application→Application/Domain；Adapter→Adapter/Application/Domain；Host→全部。保留原Core更严格约束，不因采用较宽角色规则放松既有边界。

源码检查覆盖内层生产src。识别具体request/response/extractor/public字段/type alias、运行时lifecycle、thread spawn、process/env/fs读取等Host API；普通Duration/IpAddr/crypto不按词误杀。tests目录不计生产，但cfg(feature)中的生产实现仍计；不能通过feature关掉违规代码逃避。

第三方库按中立数据/算法与具体执行技术分类，新增未分类正常依赖要求审查职责；source scan只是补充，不能仅搜tokio::spawn就宣称边界成立。典型负例必须涵盖重新命名的依赖、wrapper字段中的具体request。

## I2. 复用 check_persistence_dependency_graph.py

保留已有PG/KV/Object Store隔离规则，加入inner→local adapter/host路径检查；复用I1角色数据，不维护第二套相互冲突的名单。用cargo metadata --locked --format-version 1 --no-deps核对manifest信息，使用原cargo tree --edges normal,build检查真实依赖路径。

不把“workspace传递图任何地方都不能出现Tokio”当目标。Native feature-unification可能影响传递图，普通库也可能提供多个backend。必须阻止的是内层显式依赖/使用runtime lifecycle、公开具体实现类型以及反向依赖Adapter。

## I3. 负例与唯一owner检查

新增tests/unit/test_application_dependency_boundaries.py，标准unittest+临时manifest/source fixtures；覆盖App→Host、App→HTTP、Domain→App、alias隐藏Actix、target-specific/optionalRuntime、public wrapper、fully-qualified调用。正例为http::Method、Duration、普通crypto、ModuleLifecycle、Native调度、test executor。

按F1逐symbol记录唯一definition owner；禁止旧Adapter pub use转发；检查SendCibaResponse、OAuthJsonErrorFields、未使用RequestContext已删除。函数特定的已有source-policy路径同步更新App或Native，不能删除测试或把检查目录缩小。原nazoauth“薄binary允许依赖”规则必须按实际Host职责更新，而不是为了通过旧守卫把业务塞回错误层。