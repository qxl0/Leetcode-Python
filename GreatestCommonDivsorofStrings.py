"""
1071. Greatest Common Divisor of Strings
Easy

1279

256

Add to List

Share
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    res = sol.gcdOfStrings(str1, str2)
    print("result is: ", res)
