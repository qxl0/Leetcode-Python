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
import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[sys.maxsize] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j])
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = sol.minPathSum(grid)
    print("Ans is:", res)
