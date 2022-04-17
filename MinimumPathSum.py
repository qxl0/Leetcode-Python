"""
64. Minimum Path Sum
Medium

7142

97

Add to List

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
 
"""


import collections
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = sol.minPathSum(grid)
    print("Ans is:", res)
