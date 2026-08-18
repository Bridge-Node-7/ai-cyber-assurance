from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REFRESH_PATH = REPO_ROOT / "scripts" / "refresh_release_metadata.py"
SCRIPTS_DIR = str(REPO_ROOT / "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

spec = importlib.util.spec_from_file_location("aca_refresh_release_metadata", REFRESH_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load release metadata refresher.")
refresh = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = refresh
spec.loader.exec_module(refresh)


class ReleaseMetadataTests(unittest.TestCase):
    def make_repo(self, root: Path) -> None:
        (root / "VERSION").write_text("9.8.7\n", encoding="utf-8", newline="\n")
        (root / "README.md").write_text("# Example\n", encoding="utf-8", newline="\n")
        manifest = {
            "schema_version": "1.1",
            "repository": "ai-cyber-assurance",
            "organization": "Bridge-Node-7",
            "target_url": "https://github.com/Bridge-Node-7/ai-cyber-assurance",
            "version": "v9.8.6",
            "file_count": 0,
            "files": [],
        }
        (root / "REPO_MANIFEST.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (root / "MANIFEST.sha256").write_text("", encoding="utf-8", newline="\n")

    def test_write_then_check_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_repo(root)
            refresh.write_metadata(root)
            self.assertEqual(refresh.check_metadata(root), [])

    def test_content_change_is_detected_as_hash_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_repo(root)
            refresh.write_metadata(root)
            (root / "README.md").write_text("# Changed\n", encoding="utf-8", newline="\n")
            findings = refresh.check_metadata(root)
            self.assertTrue(any("Hash mismatch: README.md" in item for item in findings))

    def test_new_file_is_detected_as_inventory_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_repo(root)
            refresh.write_metadata(root)
            (root / "EXTRA.md").write_text("extra\n", encoding="utf-8", newline="\n")
            findings = refresh.check_metadata(root)
            self.assertTrue(any("file_count" in item or "files" in item for item in findings))

    def test_contributing_uses_deterministic_metadata_workflow(self) -> None:
        text = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("refresh_release_metadata.py --root . --write", text)
        self.assertIn("refresh_release_metadata.py --root . --check", text)
        self.assertIn("git diff --check", text)

    def test_write_preserves_human_semantic_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_repo(root)
            path = root / "REPO_MANIFEST.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["release_title"] = "Human reviewed title"
            data["release_status"] = "HUMAN_REVIEWED"
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
            refresh.write_metadata(root)
            updated = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(updated["release_title"], "Human reviewed title")
            self.assertEqual(updated["release_status"], "HUMAN_REVIEWED")


if __name__ == "__main__":
    unittest.main()
