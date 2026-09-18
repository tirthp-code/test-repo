"""Additional behavior coverage for whitespace normalization."""

import unittest

from text_normalization import normalize_whitespace


class LongInputTest(unittest.TestCase):
    def test_long_whitespace_run(self):
        """Collapse a long mixed-whitespace run without losing its boundaries."""
        self.assertEqual(normalize_whitespace('start' + ' \t\n' * 10000 + 'end'), 'start end')

    def test_many_tokens(self):
        """Keep all tokens and their order across a long input string."""
        self.assertEqual(normalize_whitespace('\t'.join(['token'] * 1000)), ' '.join(['token'] * 1000))


if __name__ == "__main__":
    unittest.main()
