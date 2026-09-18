"""Behavior coverage for count_tokens."""

import unittest

from count_tokens import count_tokens


class TextInspectionTest(unittest.TestCase):
    def test_character_and_empty_input_cases(self):
        """Check ordinary text, empty input, and Unicode whitespace."""
        cases = [('', 0), (' \t\n', 0), (' alpha\t beta\n gamma ', 3), ('alpha\xa0beta', 2), ('alpha\u200bbeta', 1)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_tokens(text), expected)


if __name__ == "__main__":
    unittest.main()
