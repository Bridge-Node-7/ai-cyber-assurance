from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_repo.py"

spec = importlib.util.spec_from_file_location("aca_validate_repo_crypto", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load repository validator.")
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class CryptographicChangeAssuranceTests(unittest.TestCase):
    def copy_crypto_surface(self, root: Path) -> None:
        shutil.copytree(
            REPO_ROOT / "12-cryptographic-change-assurance",
            root / "12-cryptographic-change-assurance",
        )
        index_dir = root / "02-evidence-manifests"
        index_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(
            REPO_ROOT / "02-evidence-manifests/review-package-index-template.md",
            index_dir / "review-package-index-template.md",
        )
        example_dir = root / "10-examples/synthetic-cryptographic-withdrawal"
        example_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            REPO_ROOT / "10-examples/synthetic-cryptographic-withdrawal",
            example_dir,
        )

    def test_current_crypto_change_surface_passes(self) -> None:
        result = validator.check_crypto_change_assurance(REPO_ROOT)
        self.assertTrue(result.passed, result.details)

    def test_missing_human_authorized_gate_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_crypto_surface(root)
            path = root / "12-cryptographic-change-assurance/cryptographic-evidence-gate.md"
            text = path.read_text(encoding="utf-8").replace("HUMAN-AUTHORIZED", "HUMAN-REVIEW")
            path.write_text(text, encoding="utf-8", newline="\n")
            result = validator.check_crypto_change_assurance(root)
            self.assertFalse(result.passed)

    def test_missing_persistent_state_class_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_crypto_surface(root)
            path = root / "12-cryptographic-change-assurance/cryptographic-change-review.md"
            text = path.read_text(encoding="utf-8").replace("**SM-4**", "**SM-X**")
            path.write_text(text, encoding="utf-8", newline="\n")
            result = validator.check_crypto_change_assurance(root)
            self.assertFalse(result.passed)

    def test_gate_order_change_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_crypto_surface(root)
            path = root / "12-cryptographic-change-assurance/cryptographic-evidence-gate.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                "QUARANTINED\n→ REPRODUCED\n→ CORROBORATED",
                "QUARANTINED\n→ CORROBORATED\n→ REPRODUCED",
                1,
            )
            path.write_text(text, encoding="utf-8", newline="\n")
            result = validator.check_crypto_change_assurance(root)
            self.assertFalse(result.passed)


if __name__ == "__main__":
    unittest.main()
