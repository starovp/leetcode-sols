"""
9. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 

There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.

"""
class Solution:
    # Runtime: 48 ms, faster than 85.48% of Python3 online submissions for Roman to Integer.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
    def romanToInt(self, s):
        # s: str
        # return: int

        # Create map of values
        roman_map = {
            'I':    1,
            'V':    5,
            'X':    10,
            'L':    50,
            'C':    100,
            'D':    500,
            'M':    1000
        }
        number = 0

        # Traverse string
        for i in range(len(s)-1):
            # If current value is less than next value, subtract it from total
            if roman_map[s[i]] < roman_map[s[i+1]]:
                number -= roman_map[s[i]]
            # Else add current value to total
            else:
                number += roman_map[s[i]]
        # Add the last number
        number += roman_map[s[-1]]
        return number

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
