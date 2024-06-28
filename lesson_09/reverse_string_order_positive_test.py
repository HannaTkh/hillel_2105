import unittest

from function_homework_09 import reverse_string_order


class ReverseStringOrderPositiveTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string_order(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string_order("a"), "a")

    def test_multiple_characters(self):
        self.assertEqual(reverse_string_order("hello"), "olleh")


if __name__ == '__main__':
    unittest.main()
