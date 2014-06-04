class RomanNumeralConverter(object):
    def convert(self, number):
        if (number >= 5):
            return "V"
        else:
            return number * "I"
