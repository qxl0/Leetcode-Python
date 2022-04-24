"""
115. Distinct Subsequences
Hard

3345

146

Add to List

Share
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the 
remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        m, n = len(t), len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(0, n + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print(f"t:{t[i-1]}  ---   s:{s[j-1]}")
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    s = "rabbbit"
    t = "rabbit"
    res = sol.numDistinct(s, t)
    print(res)
