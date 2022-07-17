from math import inf
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        cost.insert(0, [0])

        dp = [[inf] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0

        cost2 = [[0] * (1 << n) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for state in range(1 << n):
                s = 0
                for j in range(n):
                    if (state >> j) & 1:
                        s += cost[i][j]
                cost2[i][state] = s

        for i in range(1, m + 1):
            for state in range(1 << n):
                # subset
                subset = state
                while subset > 0:
                    dp[i][state] = min(
                        dp[i][state], dp[i - 1][state - subset] + cost2[i][subset]
                    )
                    subset = (subset - 1) & state
                # print(i,state,dp[i][state])
                # print(i)
                # print(cost)
                minPath = min(cost[i])
                dp[i][state] = min(dp[i][state], dp[i - 1][state] + minPath)
                # print(i, minPath, dp[i][state])
        return dp[m][(1 << n) - 1]


if __name__ == "__main__":
    sol = Solution()
    cost = [[15, 96], [36, 2]]
    res = sol.connectTwoGroups(cost)
    print(res)
