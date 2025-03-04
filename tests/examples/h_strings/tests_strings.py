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

        