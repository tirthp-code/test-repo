"""Behavior checks for display-text whitespace normalization."""

import unittest

from text_normalization import normalize_whitespace


class NormalizeWhitespaceTest(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(normalize_whitespace(""), "")

    def test_whitespace_only_input(self):
        self.assertEqual(normalize_whitespace(" \t\r\n "), "")

    def test_repeated_spaces_and_surrounding_whitespace(self):
        self.assertEqual(normalize_whitespace("  hello   world  "), "hello world")

    def test_tabs_and_line_breaks(self):
        self.assertEqual(normalize_whitespace("hello\t\nworld\r\nagain"), "hello world again")

    def test_unicode_whitespace(self):
        self.assertEqual(normalize_whitespace("hello\u00a0\u2003world"), "hello world")

    def test_preserves_non_whitespace_characters(self):
        self.assertEqual(normalize_whitespace("Hello, 世界!"), "Hello, 世界!")

    def test_normalization_is_idempotent(self):
        normalized = normalize_whitespace("  hello\t world\n ")
        self.assertEqual(normalize_whitespace(normalized), normalized)


if __name__ == "__main__":
    unittest.main()
