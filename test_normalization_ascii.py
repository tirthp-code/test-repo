"""Additional whitespace normalization regression cases."""

import unittest

from text_normalization import normalize_whitespace


class AsciiNormalizationTest(unittest.TestCase):
    def test_horizontal_spacing(self):
        """Check horizontal spacing behavior."""
        cases = [('a\tb', 'a b'), ('a\x0b\x0cb', 'a b'), ('  a  b  ', 'a b')]
        for original, expected in cases:
            with self.subTest(original=original):
                self.assertEqual(normalize_whitespace(original), expected)

    def test_multiline_spacing(self):
        """Check multiline spacing behavior."""
        cases = [('a\r\nb\nc', 'a b c'), ('\n\ra\r', 'a'), ('\t\n', '')]
        for original, expected in cases:
            with self.subTest(original=original):
                self.assertEqual(normalize_whitespace(original), expected)


if __name__ == "__main__":
    unittest.main()
