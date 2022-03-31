import math
from typing import List

"""
410. Split Array Largest Sum
Hard

5177

134

Add to List

Share
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = {}

        def dfs(i, m):
            if m == 1:
                return sum(nums[i:])
            if (i, m) in dp:
                return dp[(i, m)]
            res, curSum = float("inf"), 0
            for j in range(i, len(nums) - m + 1):
                curSum += nums[j]
                maxSum = max(curSum, dfs(j + 1, m - 1))
                res = min(res, maxSum)
                if curSum > res:
                    break
            dp[(i, m)] = res
            return res

        return dfs(0, m)


class Solution2:
    def splitArray(slef, nums, m):
        l, r = max(nums), sum(nums)

        def canSplit(y):
            numofsets = 1
            currSum = 0
            for n in range(len(nums)):
                currSum += nums[n]
                if currSum > y:
                    numofsets += 1
                    currSum = nums[n]
            return numofsets <= m

        while l < r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == "__main__":
    s = Solution2()
    nums = [7, 2, 5, 10, 8]
    m = 2
    res = s.splitArray(nums, m)
    print(res)
