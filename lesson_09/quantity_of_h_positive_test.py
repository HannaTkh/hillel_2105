import unittest

from function_homework_09 import quantity_of_h


class QuantityOfhPositiveTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(quantity_of_h(""), 0)

    def test_one_h(self):
        self.assertEqual(quantity_of_h("hello"), 1)

    def test_multiple_h(self):
        self.assertEqual(quantity_of_h("hhhhhh"), 6)


if __name__ == '__main__':
    unittest.main()
