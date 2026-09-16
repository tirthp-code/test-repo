"""Additional whitespace normalization regression cases."""

import unittest

from text_normalization import normalize_whitespace


class UnicodeNormalizationTest(unittest.TestCase):
    def test_unicode_separators(self):
        """Check unicode separators behavior."""
        cases = [('a\xa0b', 'a b'), ('a\u2002\u2003b', 'a b'), ('a\u2028\u2029b', 'a b')]
        for original, expected in cases:
            with self.subTest(original=original):
                self.assertEqual(normalize_whitespace(original), expected)

    def test_unicode_boundaries(self):
        """Check unicode boundaries behavior."""
        cases = [('\u3000hello\u3000', 'hello'), ('\u2003\xa0', ''), ('\u202fhello\u205fworld', 'hello world')]
        for original, expected in cases:
            with self.subTest(original=original):
                self.assertEqual(normalize_whitespace(original), expected)


if __name__ == "__main__":
    unittest.main()
