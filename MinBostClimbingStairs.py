"""
746. Min Cost Climbing Stairs
Easy

5802

1007

Add to List

Share
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 
"""


import collections
import heapq
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    cost = [10, 15, 20]
    res = sol.minCostClimbingStairs(cost)
    print("result is: ", res)
