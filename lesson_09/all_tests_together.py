import unittest

from function_homework_09 import *


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


class AverageNegativeTest(unittest.TestCase):

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            average("hello")

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            average(10)


class ReverseStringOrderPositiveTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string_order(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string_order("a"), "a")

    def test_multiple_characters(self):
        self.assertEqual(reverse_string_order("hello"), "olleh")


class ReverseStringOrderNegativeTest(unittest.TestCase):

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            reverse_string_order(123)


class QuantityOfhPositiveTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(quantity_of_h(""), 0)

    def test_one_h(self):
        self.assertEqual(quantity_of_h("hello"), 1)

    def test_multiple_h(self):
        self.assertEqual(quantity_of_h("hhhhhh"), 6)


if __name__ == '__main__':
    unittest.main()
