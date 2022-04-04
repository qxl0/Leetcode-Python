"""
567. Permutation in String
Medium

5585

162

Add to List

Share
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    s1 = "ab"
    s2 = "eidaooo"
    res = sol.checkInclusion(s1, s2)
    print(res)
