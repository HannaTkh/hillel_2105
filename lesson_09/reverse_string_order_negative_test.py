import unittest

from function_homework_09 import reverse_string_order


class ReverseStringOrderNegativeTest(unittest.TestCase):

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            reverse_string_order(123)


if __name__ == '__main__':
    unittest.main()
