"""
122. Best Time to Buy and Sell Stock II
Medium

7216

2351

Add to List

Share
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp, l = 0, 0
        for i in range(1, len(prices)):
            if prices[i] > prices[l]:
                maxp += prices[i] - prices[l]
                l = i
            else:
                l = i
        return maxp


if __name__ == "__main__":
    sol = Solution()
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2, 3]
    res = sol.maxProfit(prices)
    print(res)
