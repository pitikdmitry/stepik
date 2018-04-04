from .lzw import *
import sys
import unittest


class LwzTest(unittest.TestCase):

    def test_simple(self):
        print("")
        input_str = "abacabadabacabae"
        coded_str, returned_str = run_programm(input_str)
        self.assertEqual(input_str, returned_str)
        print("size before: " + str(sys.getsizeof(input_str)))
        print("size after: " + str(sys.getsizeof(coded_str)))
        print("")

    # def test_with_space(self):
    #     print("")
    #     input_str = "abacaba" + " dabac, abae"
    #     coded_str, returned_str = run_programm(input_str)
    #     self.assertEqual(input_str, returned_str)
    #     print("size before: " + str(sys.getsizeof(input_str)))
    #     print("size after: " + str(sys.getsizeof(returned_str)))
    #     print("")
    #
    # def test_big_str(self):
    #     print("")
    #     input_str = "abacarejkgnerkljgbrjeklbasaagavafcacafaafcaaaafvavabababbaba" + " dabac, abae"
    #     coded_str, returned_str = run_programm(input_str)
    #     self.assertEqual(input_str, returned_str)
    #     print("size before: " + str(sys.getsizeof(input_str)))
    #     print("size after: " + str(sys.getsizeof(coded_str)))
    #     print("length before: " + str(len(input_str)))
    #     print("length after: " + str(len(returned_str)))
    #     print("")
