from collections import defaultdict
from typing import Counter, List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dp = [[set()] * n for _ in range(m)]
        if grid[0][0] == "(":
            dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                k = 1 if grid[i][j] == "(" else -1
                if j >= 1:
                    # print(dp[i][j-1])
                    for x in dp[i][j - 1]:
                        if x + k >= 0 and (m + n + 1 - (i + j + 1)) >= x + k:
                            dp[i][j].add(x + k)
                if i >= 1:
                    for x in dp[i - 1][j]:
                        if x + k >= 0 and (m + n + 1 - (i + j + 1)) >= x + k:
                            dp[i][j].add(x + k)
        print(dp)
        return 0 in dp[m - 1][n - 1]

    def hasValidPath2(self, A):
        m, n = len(A), len(A[0])
        dp = defaultdict(set)
        dp[0, -1] = dp[-1, 0] = {0}
        for i in range(m):
            for j in range(n):
                d = 1 if A[i][j] == "(" else -1
                dp[i, j] |= {a + d for a in dp[i - 1, j] | dp[i, j - 1] if a + d >= 0}
        return 0 in dp[m - 1, n - 1]


if __name__ == "__main__":
    sol = Solution()
    grid = [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]
    res = sol.hasValidPath2(grid)
    print("result is: ", res)
