"""
63. Unique Paths II
Medium

4536

372

Add to List

Share
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
 
"""


import collections
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == j == 0:  # dp[0][0]=1
                        dp[i][j] = 1
                        continue
                    else:  # hidden: [-1][j]=0 and dp[i][-1]=0 since dp = [ [0]*n for _ in range(m) ]
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    print("Ans is:", res)
