"""
95. Unique Binary Search Trees II
Medium

4630

303

Add to List

Share
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    n = 3
    res = sol.generateTrees(n)
    print(res)
