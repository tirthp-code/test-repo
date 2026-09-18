"""Behavior coverage for count_blank_lines."""

import unittest

from count_blank_lines import count_blank_lines


class TextInspectionTest(unittest.TestCase):
    def test_character_and_empty_input_cases(self):
        """Check ordinary text, empty input, and Unicode whitespace."""
        cases = [('', 0), ('\n', 1), ('alpha\n \t\nbeta\n\n', 2), ('\xa0\n', 1), ('alpha\n', 0)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_blank_lines(text), expected)


if __name__ == "__main__":
    unittest.main()
