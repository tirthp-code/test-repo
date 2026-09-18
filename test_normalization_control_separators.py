"""Additional behavior coverage for whitespace normalization."""

import unittest

from text_normalization import normalize_whitespace


class ControlSeparatorsTest(unittest.TestCase):
    def test_ascii_control_separators(self):
        """Collapse ASCII whitespace control characters to one space."""
        for separator in ('\t', '\n', '\v', '\f', '\r', '\x1c', '\x1d', '\x1e', '\x1f'):
            with self.subTest(separator=repr(separator)):
                self.assertEqual(normalize_whitespace(separator + 'left' + separator * 3 + 'right' + separator), 'left right')


if __name__ == "__main__":
    unittest.main()
