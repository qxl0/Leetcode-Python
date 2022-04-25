"""
940. Distinct Subsequences II
Hard

1080

27

Add to List

Share
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    res = sol.distinctSubseqII(s)
    print(res)
