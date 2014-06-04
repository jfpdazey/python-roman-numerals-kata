class RomanNumeralConverter(object):
    def convert(self, number):
        roman_numeral = ""
        
        if (number >= 5):
            roman_numeral = "V"
            number = number -  5

        roman_numeral = roman_numeral + (number * "I")

        return roman_numeral
