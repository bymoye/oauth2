use super::*;
use nazo_key_management::{KeyManager, Openid4vcPublicMaterial, TestSigningBehavior};

fn signing_lease(behavior: TestSigningBehavior) -> Openid4vcSigningLease {
    let keyset = KeyManager::for_test_behavior(jsonwebtoken::Algorithm::ES256, behavior);
    keyset.set_openid4vc_material_for_test(Openid4vcPublicMaterial {
        signing_kid: keyset.snapshot().active_kid.clone(),
        certificate_chain_pem: String::new(),
        trust_anchors_pem: String::new(),
        revocation_snapshot: None,
    });
    keyset
        .prepare_openid4vc_signing()
        .expect("fixture signing lease")
}

#[test]
fn async_cose_signer_uses_credential_scope_and_propagates_signing_errors() {
    let runtime = tokio::runtime::Runtime::new().expect("test runtime");
    let signer = AsyncCoseSigner {
        lease: signing_lease(TestSigningBehavior::Working),
        certificate_der: vec![1, 2, 3],
        runtime: runtime.handle().clone(),
    };
    let signature = signer.sign(b"credential tbs").expect("signature");
    assert_eq!(signature.len(), 64);
    assert_eq!(signer.algorithm(), -7);
    assert_eq!(signer.certificate_der(), &[1, 2, 3]);
    let failing = AsyncCoseSigner {
        lease: signing_lease(TestSigningBehavior::Failing),
        certificate_der: vec![1, 2, 3],
        runtime: runtime.handle().clone(),
    };
    assert!(failing.sign(b"credential tbs").is_err());
}
