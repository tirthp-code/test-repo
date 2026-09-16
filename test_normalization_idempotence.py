"""Exercise idempotence across varied whitespace normalization inputs."""

import unittest

from text_normalization import normalize_whitespace


class IdempotenceTest(unittest.TestCase):
    def test_normalizing_twice_keeps_the_same_result(self):
        """A second pass preserves the result of the first normalization."""
        cases = ["", "one", "  one   two  ", "one\ttwo\nthree", "\u3000café\u00a0世界\u3000"]
        for original in cases:
            with self.subTest(original=original):
                once = normalize_whitespace(original)
                self.assertEqual(normalize_whitespace(once), once)


if __name__ == "__main__":
    unittest.main()
