import unittest

from integer_magnitude import integer_magnitude


class IntegerUtilityTest(unittest.TestCase):
    def test_negative_zero_and_positive_inputs(self):
        for number, expected in [(-10, 10), (-1, 1), (0, 0), (1, 1), (10, 10)]:
            with self.subTest(number=number):
                self.assertEqual(integer_magnitude(number), expected)


if __name__ == "__main__":
    unittest.main()
