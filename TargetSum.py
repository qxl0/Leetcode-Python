"""
474. Ones and Zeroes
Medium

2874

324

Add to List

Share
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)

        def subsetSum(t):
            # dp[i] represents # of ways to add up to i from nums
            # dp[i] = sum(dp[i-n], for n in nums where i>=n)
            dp = [0] * (t + 1)
            dp[0] = 1
            for n in nums:
                for j in range(t, -1, -1):
                    if j >= n:
                        dp[j] += dp[j - n]
            print(dp)
            return dp[t]

        if target > s or (s + target) % 2 == 1:
            return 0
        return subsetSum((s + target) // 2)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    res = sol.findTargetSumWays(nums, target)

    print(res)
