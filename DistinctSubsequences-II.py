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


MOD = 10**9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1] * len(s)
        last = {c: i for i, c in enumerate(s)}

        for i in range(1, len(s)):
            dp[i] = (2 * dp[i - 1]) % MOD
            if 0 < last[s[i]] < i:
                dp[i] -= dp[last[s[i]] - 1]

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    res = sol.distinctSubseqII(s)
    print(res)
