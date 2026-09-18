"""Additional behavior coverage for whitespace normalization."""

import unittest

from text_normalization import normalize_whitespace


class CombiningContentTest(unittest.TestCase):
    def test_combining_marks_and_emoji(self):
        """Leave grapheme content unchanged across whitespace normalization."""
        self.assertEqual(normalize_whitespace('  cafe\u0301\t  👩‍💻\n  🇮🇳  '), 'cafe\u0301 👩‍💻 🇮🇳')


if __name__ == "__main__":
    unittest.main()
