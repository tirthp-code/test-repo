import unittest

from integer_sign import integer_sign


class IntegerUtilityTest(unittest.TestCase):
    def test_negative_zero_and_positive_inputs(self):
        for number, expected in [(-100, -1), (-1, -1), (0, 0), (1, 1), (100, 1)]:
            with self.subTest(number=number):
                self.assertEqual(integer_sign(number), expected)


if __name__ == "__main__":
    unittest.main()
