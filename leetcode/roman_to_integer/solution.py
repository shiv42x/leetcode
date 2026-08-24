class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        accum = 0
        previous_roman = ''
        for current_roman in s:
            prev = roman_to_int.get(previous_roman) #10
            curr = roman_to_int.get(current_roman) #100
            previous_roman = current_roman
            
            if not prev:
                accum += curr
                continue
            
            accum += curr

            if prev < curr:
                accum -= (prev * 2)

        return accum 
