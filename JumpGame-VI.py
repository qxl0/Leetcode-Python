"""
1696. Jump Game VI
Medium

1313

52

Add to List

Share
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 
"""
import collections
import sys
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # dp[i] represents the maximum score you can get reaching to index i
        # dp[0]
        # dp[i] = max(dp[j]+nums[i] for all j within k steps)
        dp = [-sys.maxsize / 2] * n
        dp[0] = nums[0]
        for i in range(1, n):
            for j in range(i - k, i, 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return dp[n - 1]


class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dq = collections.deque()
        dq.append(0)
        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = dp[dq[0]] + nums[i]
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            dq.append(i)
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, -5, -20, 4, -1, 3, -6, -3]
    k = 2
    res = sol.maxResult(nums, k)
    print("Ans is : ", res)
