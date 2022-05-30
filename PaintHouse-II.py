"""
265. Paint House II
Hard

1005

33

Add to List

Share
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.
"""
import math
import sys
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, k = len(costs), len(costs[0])
        if m == 0:
            return 0
        # dp[i][k] represents minimum cost to
        dp = [[sys.maxsize] * (k + 1) for _ in range(m + 1)]
        for j in range(k):
            dp[0][j] = costs[0][j]

        for i in range(1, m):
            for color in range(k):
                best = math.inf
                for prev in range(k):
                    if color == prev:
                        continue
                    best = min(best, dp[i - 1][prev])
                dp[i][color] = best + costs[i][color]

        return min(dp[m - 1])


if __name__ == "__main__":
    s = Solution()
    costs = [
        [20, 19, 11, 13, 12, 16, 16, 17, 15, 9, 5, 18],
        [3, 8, 15, 17, 19, 8, 18, 3, 11, 6, 7, 12],
        [15, 4, 11, 1, 18, 2, 10, 9, 3, 6, 4, 15],
    ]
    res = s.minCostII(costs)
    print(res)
