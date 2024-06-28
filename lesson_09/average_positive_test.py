import unittest

from function_homework_09 import average


class AveragePositiveTest(unittest.TestCase):

    def test_empty_list(self):
        expected_result = 0
        input_param = []
        self.assertEqual(average(input_param), expected_result)

    def test_negative_numbers(self):

        expected_result = -20
        input_param = [-10, -20, -30]

        self.assertEqual(average(input_param), expected_result)

    def test_single_number(self):

        expected_result = 5
        input_param = [5]

        self.assertEqual(average(input_param), expected_result)

    def test_decimal_numbers(self):

        expected_result = 2.5
        input_param = [1.5, 2.5, 3.5]


        self.assertEqual(average(input_param), expected_result)


if __name__ == '__main__':
    unittest.main()