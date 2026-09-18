import unittest

from is_even import is_even


class IntegerUtilityTest(unittest.TestCase):
    def test_negative_zero_and_positive_inputs(self):
        for number, expected in [(-4, True), (-3, False), (0, True), (3, False), (4, True)]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), expected)


if __name__ == "__main__":
    unittest.main()
