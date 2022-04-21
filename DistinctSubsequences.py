"""
115. Distinct Subsequences
Hard

3345

146

Add to List

Share
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    s = "rabbbit"
    t = "rabbit"
    res = sol.numDistinct(s, t)
    print(res)
