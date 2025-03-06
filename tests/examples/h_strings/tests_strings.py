import unittest

from src.examples.h_strings.strings import string_params, string_return_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_params(self):
        strl = "Python"

        string_params(strl)
        self.assertEqual(strl, "Python")

        strl = "C++"
        self.assertEqual(strl, "C++")

    def test_string_return_value(self):
        lang = "Python"

        lang1 = string_return_value(lang)
        print(id(lang1))

        self.assertEqual(lang, "Python")
        self.assertEqual(lang1, "C++")

    def test_search_string_w_in(self):
        text = "Four score and seven years ago"

        is_in = 'seven' in text

        self.assertEqual(is_in, True) 

    def test_search_string_w_in(self):
        text = "Four score and seven years ago"

        is_in = 'Seven' in text

        self.assertEqual(is_in, False)

    def test_search_w_not_in(self):
        text = "Four score and seven years ago"

        not_in = 'Seven' not in text

        self.assertEqual(not_in, True)

    def test_string_isdigit(self):
        str = "123"

        self.assertEqual(str.isdigit(), True)

    def test_string_not_isdigit(self):
        str = "OneTwoThree"

        self.assertEqual(str.isdigit(), False)

    def test_string_isupper(self):
        str = "OneTwoThree"

        self.assertEqual(str.isupper(), False)

    