import unittest
from src.roman_numeral_converter import RomanNumeralConverter

class RomanNumeralConverterTest(unittest.TestCase):
    def test_converts_one(self):
        self.assertEquals(RomanNumeralConverter().convert(1), "I")

if __name__ == '__main__':
    unittest.main()
