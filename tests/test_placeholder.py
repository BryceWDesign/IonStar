"""
Basic sanity test for the IonStar package.

Run via:  python -m unittest discover tests
"""

import importlib
import unittest


class TestImport(unittest.TestCase):
    def test_import_main(self):
        """Ensure the main control module imports without error."""
        module = importlib.import_module("src.main")
        self.assertTrue(hasattr(module, "main"))


if __name__ == "__main__":
    unittest.main()
