"""Additional behavior coverage for whitespace normalization."""

import unittest

from text_normalization import normalize_whitespace


class ZeroWidthTest(unittest.TestCase):
    def test_zero_width_characters_are_content(self):
        """Keep zero-width content intact while normalizing surrounding spaces."""
        for character in ('\u200b', '\u200c', '\u200d', '\ufeff'):
            with self.subTest(character=repr(character)):
                self.assertEqual(normalize_whitespace('  left' + character + 'right  '), 'left' + character + 'right')


if __name__ == "__main__":
    unittest.main()
