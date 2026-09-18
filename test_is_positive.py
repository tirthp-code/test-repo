import unittest

from is_positive import is_positive


class IntegerUtilityTest(unittest.TestCase):
    def test_negative_zero_and_positive_inputs(self):
        for number, expected in [(-10, False), (-1, False), (0, False), (1, True), (10, True)]:
            with self.subTest(number=number):
                self.assertEqual(is_positive(number), expected)


if __name__ == "__main__":
    unittest.main()
