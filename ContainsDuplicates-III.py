"""
220. Contains Duplicate III
Medium

2305

2239

Add to List

Share
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
"""

from math import floor
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    print("Ans is: ", res)
