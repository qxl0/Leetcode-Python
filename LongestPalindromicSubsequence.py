"""
516. Longest Palindromic Subsequence
Medium

5073

246

Add to List

Share
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def longestPalindromeSubseq(self, s):
            d = {}

            def f(s):
                if s not in d:
                    maxL = 0
                    for c in set(s):
                        i, j = s.find(c), s.rfind(c)
                        maxL = max(maxL, 1 if i == j else 2 + f(s[i + 1 : j]))
                    d[s] = maxL
                return d[s]

            return f(s)


if __name__ == "__main__":
    sol = Solution()
    s = "bbbab"
    res = sol.longestPalindromeSubseq(s)
    print(res)
