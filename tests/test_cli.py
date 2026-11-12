import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CommandLineTests(unittest.TestCase):
    def test_example(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "rover.py"), str(ROOT / "input.txt")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "1 3 N\n5 1 E\n")
        self.assertEqual(result.stderr, "")

    def test_missing_file(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "rover.py"), str(ROOT / "missing.txt")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("Erreur :", result.stderr)


if __name__ == "__main__":
    unittest.main()
