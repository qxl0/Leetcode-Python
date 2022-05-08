"""
456. 132 Pattern
Medium

4513

250

Add to List

Share
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

from this import d
from typing import List, Optional


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 1, 4, 2]
    res = sol.find132pattern(nums)
    print(res)
