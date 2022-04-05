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
        pass


if __name__ == "__main__":
    sol = Solution()
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    res = sol.maxProfit(prices)
    print(res)
