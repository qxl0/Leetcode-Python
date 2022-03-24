"""
62. Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    # exceed time limits
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def helper(m, n):
            if m == 1 or n == 1:
                return 1
            if dp[m][n] > 0:
                return dp[m][n]
            dp[m][n] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
            return dp[m][n]

        return helper(m, n)

    def uniquePaths2(self, m, n):
        if not m or not n:
            return 0
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    m = 2
    n = 2
    res = sol.uniquePaths2(m, n)
    print("result is: ", res)
