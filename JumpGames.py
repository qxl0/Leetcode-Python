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
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 1, 4]
    res = sol.canJump(nums)
    print("result is: ", res)
