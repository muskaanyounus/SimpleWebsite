class RomanConverter:
     def __init__(self):
         self.roman_numerals = [
             (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
             (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
         ]
 
     def int_to_roman(self, num):
         if not (1 <= num <= 3999):
             raise ValueError("Input integer must be between 1 and 3999")
         
         roman = ''
         for value, numeral in self.roman_numerals:
             while num >= value:
                 roman += numeral
                 num -= value
         return roman
 
     def roman_to_int(self, roman):
         roman_to_int_map = {
             'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
             'D': 500, 'M': 1000
         }
         
         total = 0
         prev_value = 0
         
         for char in reversed(roman):
             value = roman_to_int_map[char]
             if value < prev_value:
                 total -= value
             else:
                 total += value
             prev_value = value
         
         return total
 
 converter = RomanConverter()
 
 print(converter.int_to_roman(1994))  
 
 print(converter.roman_to_int('MCMXCIV'))  