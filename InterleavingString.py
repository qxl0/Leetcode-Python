"""
97. Interleaving String
Medium

3797

202

Add to List

Share
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        dp = {}

        def dfs(i, j):  # s1[i:] s2[j:] is interleave s3[i+j:]
            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True
            if i + j >= len(s3):
                dp[(i, j)] = False
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False
            return False

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    s1 = "a"
    s2 = "b"
    s3 = "a"
    res = sol.isInterleave(s1, s2, s3)
    print(res)
