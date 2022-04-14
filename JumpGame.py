"""
55. Jump Game
Medium

10598

613

Add to List

Share
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
import sys
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] stands for whether you can reach index i from the first index
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
        print(f"{dp}")
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    res = s.canJump(nums)
    print("Ans is : ", res)
