from .lzw_words import *
import sys
import os
import unittest


class LwzTest(unittest.TestCase):

    def get_str_from_filename(self, filename: str) -> str:
        text = ""
        with open(filename, 'r') as f:
            for line in f:
                text += line

        return text

    # def test_simple(self):
    #     print("simple test: ")
    #     input_str = "abacabadabacabae"
    #     coded_str, decoded_str = run_programm(input_str)
    #     self.assertEqual(input_str, decoded_str)
    #     print("size input: " + str(sys.getsizeof(input_str)))
    #     print("size coded: " + str(sys.getsizeof(coded_str)))
    #     print("")
    #
    # def test_with_space(self):
    #     print("test with space: ")
    #     input_str = "i went somewhere"
    #     coded_str, decoded_str = run_programm(input_str)
    #     self.assertEqual(input_str, decoded_str)
    #     print("size input: " + str(sys.getsizeof(input_str)))
    #     print("size coded: " + str(sys.getsizeof(coded_str)))
    #     print("")
    #
    # def test_special_symbols(self):
    #     print("test_special_symbols: ")
    #     input_str = "\n\r\t;.,/12345679-098`"
    #     coded_str, decoded_str = run_programm(input_str)
    #     self.assertEqual(input_str, decoded_str)
    #     print("size input: " + str(sys.getsizeof(input_str)))
    #     print("size coded: " + str(sys.getsizeof(coded_str)))
    #     print("")
    #
    # def test_big_str(self):
    #     print("big str test: ")
    #     input_str = ", и он начинал бредить."
    #     coded_str, decoded_str = run_programm(input_str)
    #     self.assertEqual(input_str, decoded_str)
    #     print("size input: " + str(sys.getsizeof(input_str)))
    #     print("size coded: " + str(sys.getsizeof(coded_str)))
    #     print("")

    def test_all_files(self):
        dir = os.getcwd()
        for filename in os.listdir(os.getcwd()):
            if filename[-4:] == ".txt":
                header_str = str(filename) + " : "
                print(header_str)
                input_str = self.get_str_from_filename(filename)
                coded_str, decoded_str = run_programm(input_str)
                self.assertEqual(input_str, decoded_str)
                print("size input: " + str(sys.getsizeof(input_str)))
                print("size coded: " + str(sys.getsizeof(coded_str)))
                print("")
