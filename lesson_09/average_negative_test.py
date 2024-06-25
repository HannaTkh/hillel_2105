import unittest

from function_homework_09 import average


class AverageNegativeTest(unittest.TestCase):

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            average("hello")

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            average(10)


if __name__ == '__main__':
    unittest.main()
