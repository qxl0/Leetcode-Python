"""
65. Valid Number
Hard

556

995

Add to List

Share
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
 
"""


import collections
import sys
from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        sign, digit, e, dec = False, False, False, False

        for c in s:
            if c in "0123456789":
                digit = True
            elif c in "+-":
                if digit or sign or digit or dec:
                    return False
                sign = True
            elif c in "eE":
                if e or not digit:
                    return False
                e = True
                sign = False
                digit = False
                dec = False
            elif c == ".":
                if dec or e:
                    return False
                dec = True
            else:
                return False
        return digit


if __name__ == "__main__":
    sol = Solution()
    s = "0"
    res = sol.isNumber(s)
    print("Ans is:", res)
