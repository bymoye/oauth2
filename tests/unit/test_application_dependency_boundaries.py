from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("application_guards", ROOT / "scripts" / "verify_static_contracts.py")
GUARDS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARDS)


class ApplicationDependencyBoundaries(unittest.TestCase):
    def assert_manifest_boundary(self, package: str, dependencies: str, rejected: bool) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "Cargo.toml").write_text('[workspace]\n[workspace.dependencies]\nhidden = { package = "nazoauth", path = "crates/host" }\n')
            crate = root / "crates" / "consumer"
            crate.mkdir(parents=True)
            (crate / "Cargo.toml").write_text(f'[package]\nname = "{package}"\n' + dependencies)
            with patch.object(GUARDS, "ROOT", root):
                if rejected:
                    with self.assertRaises(SystemExit):
                        GUARDS.check_package_roles()
                else:
                    GUARDS.check_package_roles()

    def test_application_rejects_host_and_http_adapter(self) -> None:
        for dependency in ("nazoauth", "nazo-http-actix"):
            with self.subTest(dependency=dependency):
                self.assert_manifest_boundary("nazo-oauth-server", f'[dependencies]\n{dependency} = "1"\n', True)

    def test_domain_rejects_application(self) -> None:
        self.assert_manifest_boundary("nazo-identity", '[dependencies]\nnazo-oauth-server = "1"\n', True)

    def test_workspace_alias_cannot_hide_host(self) -> None:
        self.assert_manifest_boundary("nazo-oauth-server", '[dependencies]\nhidden.workspace = true\n', True)

    def test_optional_target_build_dependency_cannot_hide_adapter(self) -> None:
        self.assert_manifest_boundary("nazo-oauth-server", '[target.\'cfg(unix)\'.build-dependencies]\nhidden = { package = "nazo-http-actix", version = "1", optional = true }\n', True)

    def test_native_composition_and_application_domain_dependencies_are_allowed(self) -> None:
        self.assert_manifest_boundary("nazoauth", '[dependencies]\nnazo-http-actix = "1"\n', False)
        self.assert_manifest_boundary("nazo-oauth-server", '[dependencies]\nnazo-identity = "1"\nhttp = "1"\n', False)

    def test_dev_executor_is_not_a_production_edge(self) -> None:
        self.assert_manifest_boundary("nazo-oauth-server", '[dev-dependencies]\nfutures-executor = "1"\n', False)
