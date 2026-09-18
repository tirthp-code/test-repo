"""Behavior coverage for has_whitespace."""

import unittest

from has_whitespace import has_whitespace


class TextInspectionTest(unittest.TestCase):
    def test_character_and_empty_input_cases(self):
        """Check ordinary text, empty input, and Unicode whitespace."""
        cases = [('', False), ('abc', False), ('a\tb', True), ('a\xa0b', True), ('a\u200bb', False)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(has_whitespace(text), expected)


if __name__ == "__main__":
    unittest.main()
