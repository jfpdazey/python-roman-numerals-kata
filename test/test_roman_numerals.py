import unittest
from src.roman_numeral_converter import RomanNumeralConverter

class RomanNumeralConverterTest(unittest.TestCase):
    def test_converts_one(self):
        self.assertEquals(RomanNumeralConverter().convert(1), "I")

    def test_converts_two(self):
        self.assertEquals(RomanNumeralConverter().convert(2), "II")

if __name__ == '__main__':
    unittest.main()
