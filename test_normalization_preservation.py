"""Additional whitespace normalization regression cases."""

import unittest

from text_normalization import normalize_whitespace


class PreservationNormalizationTest(unittest.TestCase):
    def test_punctuation(self):
        """Check punctuation behavior."""
        cases = [(' Hello,  world! ', 'Hello, world!'), ('a/b:c_d-e', 'a/b:c_d-e'), ('a\t(b)\n[c]', 'a (b) [c]')]
        for original, expected in cases:
            with self.subTest(original=original):
                self.assertEqual(normalize_whitespace(original), expected)

    def test_unicode_content(self):
        """Check unicode content behavior."""
        cases = [('  世界  café  ', '世界 café'), ('👋\t🌍', '👋 🌍'), ('a\u200bb', 'a\u200bb')]
        for original, expected in cases:
            with self.subTest(original=original):
                self.assertEqual(normalize_whitespace(original), expected)


if __name__ == "__main__":
    unittest.main()
