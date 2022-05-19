"""
416. Partition Equal Subset Sum
Medium

7450

118

Add to List

Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        total //= 2
        n = len(nums)
        dp = [[False] * (total + 1) for _ in range(n + 1)]  # dp[i][w]: goal is total
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, total + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][total]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 11, 5]
    res = sol.canPartition(nums)

    print(res)
