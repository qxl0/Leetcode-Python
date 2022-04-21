"""
120. Triangle
Medium

4804

380

Add to List

Share
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    res = sol.minimumTotal(triangle)
    print(res)
