"""
13. Roman to Integer
Easy

3645

257

Add to List

Share
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


import enum
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IV", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += roman2int[char]
        return number


class Solution2:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for c in s[::-1]:
            if d[c] >= prev:  # IV-->4 = 5-1 IX --> 10-1=9 XL-->50-10=40
                res += d[c]
            else:
                res -= d[c]
            prev = d[c]
        return res


class Solution3:
    def romanToInt(self, s):
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        for idx, char in enumerate(
            s[:-1]
        ):  # only goes next last, because we look ahead 1 pos
            if d[char] < d[s[idx + 1]]:
                value -= d[char]
            else:
                value += d[char]
        # value += d[s[-1]]
        return value


if __name__ == "__main__":
    sol = Solution3()
    # s = "LIV"
    s = "IX"
    res = sol.romanToInt(s)
    print(res)
