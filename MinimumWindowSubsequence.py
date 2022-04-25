"""
727. Minimum Window Subsequence
Hard

1229

74

Add to List

Share
Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s1 = "abcdebdde"
    s2 = "bde"
    res = sol.minWindow(s1, s2)
    print(res)
