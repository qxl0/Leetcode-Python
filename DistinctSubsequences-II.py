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
import enum
from math import factorial
from operator import itemgetter
from typing import List


MOD = 10**9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        last = {}
        dp = [1]

        for i, c in enumerate(s):
            dp.append(dp[-1] * 2)
            if c in last:
                dp[-1] -= dp[last[c]]
            last[c] = i
        print(dp)
        return (dp[-1] - 1) % MOD


class Solution2:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26
        for c in s:
            dp[ord(c) - ord("a")] = (sum(dp) + 1) % MOD
        return sum(dp)


if __name__ == "__main__":
    sol = Solution()
    # s = "aba"  # 6
    s = "cbab"
    res = sol.distinctSubseqII(s)
    print(res)
