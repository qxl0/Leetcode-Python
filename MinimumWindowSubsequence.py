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
from re import I
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)
        dp = [[-1] * tlen for _ in range(slen)]
        for i in range(slen):
            if s[i] == t[0]:
                dp[i][0] = i
            else:
                if i != 0:
                    dp[i][0] = dp[i - 1][0]
        # dp
        for i in range(1, slen):
            for j in range(1, tlen):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp)
        # get  dp[i][tlen-1]
        begin = -1
        minlen = float("inf")
        for i in range(slen):
            k = dp[i][tlen - 1]
            if k != -1:
                cur = i - k + 1
                if cur < minlen:
                    begin, minlen = k, cur
        if begin == -1:
            return ""
        return s[begin : begin + minlen]


if __name__ == "__main__":
    sol = Solution()
    # s1 = "abcdebdde"
    # s2 = "bde"
    # s1 = "lmkl"
    # s2 = "l"
    s = "ngpkbrofkbkoacqjqjmfohikc"
    t = "n"
    res = sol.minWindow(s, t)
    print(res)
