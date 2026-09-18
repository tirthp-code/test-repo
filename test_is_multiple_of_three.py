import unittest

from is_multiple_of_three import is_multiple_of_three


class IntegerUtilityTest(unittest.TestCase):
    def test_negative_zero_and_positive_inputs(self):
        for number, expected in [(-6, True), (-2, False), (0, True), (2, False), (6, True)]:
            with self.subTest(number=number):
                self.assertEqual(is_multiple_of_three(number), expected)


if __name__ == "__main__":
    unittest.main()
