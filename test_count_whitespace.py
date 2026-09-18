"""Behavior coverage for count_whitespace."""

import unittest

from count_whitespace import count_whitespace


class TextInspectionTest(unittest.TestCase):
    def test_character_and_empty_input_cases(self):
        """Check ordinary text, empty input, and Unicode whitespace."""
        cases = [('', 0), ('a b\t\nc', 3), ('\xa0a\u2003', 2), ('a\u200bb', 0)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_whitespace(text), expected)


if __name__ == "__main__":
    unittest.main()
