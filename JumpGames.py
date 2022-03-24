"""
55. Jump Game
Medium

10318

604

Add to List

Share
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


from typing import List


class Solution:
    # exceed time limits
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if dp[j] and nums[j] >= i - j:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    res = sol.canJump(nums)
    print("result is: ", res)
