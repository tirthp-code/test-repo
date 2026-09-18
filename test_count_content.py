"""Behavior coverage for count_content."""

import unittest

from count_content import count_content


class TextInspectionTest(unittest.TestCase):
    def test_character_and_empty_input_cases(self):
        """Check ordinary text, empty input, and Unicode whitespace."""
        cases = [('', 0), ('a b\t\nc', 3), ('\xa0a\u2003', 1), ('a\u200bb', 3)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_content(text), expected)


if __name__ == "__main__":
    unittest.main()
