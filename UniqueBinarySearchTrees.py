"""
96. Unique Binary Search Trees
Medium

7056

287

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * (n + 1)
        res[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]

        return res[n]


if __name__ == "__main__":
    sol = Solution()
    n = 3
    res = sol.numTrees(n)
    print(res)
