import unittest
from src.roman_numeral_converter import RomanNumeralConverter

class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.my_converter = RomanNumeralConverter()

    def test_converts_one(self):
        self.assertEquals(self.my_converter.convert(1), "I")

    def test_converts_two(self):
        self.assertEquals(self.my_converter.convert(2), "II")

    def test_converts_five(self):
        self.assertEquals(self.my_converter.convert(5), "V")

    def test_converts_six(self):
        self.assertEquals(self.my_converter.convert(6), "VI")

if __name__ == '__main__':
    unittest.main()
