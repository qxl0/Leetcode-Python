"""
123. Best Time to Buy and Sell Stock III
Hard

5608

114

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for i in range(len(prices))]
        for i in range(1, 2 + 1):
            pos = -prices[0]
            profit = 0
            for t in range(1, len(prices)):
                pos = max(pos, dp[t] - prices[t])
                profit = max(profit, pos + prices[t])
                dp[t] = profit
        return dp[len(prices) - 1]
        # return profit


class Solution2:
    def maxProfit(self, prices):
        if not prices:
            return 0
        s1, s2, s3, s4 = (
            -prices[0],
            -float("inf"),
            -float("inf"),
            -float("inf"),
        )

        for p in prices:
            s1 = max(s1, -p)
            s2 = max(s2, s1 + p)
            s3 = max(s3, s2 - p)
            s4 = max(s4, s3 + p)
        return s4


if __name__ == "__main__":
    sol = Solution()
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    res = sol.maxProfit(prices)
    print(res)
