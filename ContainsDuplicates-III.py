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
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getID(x, w):
            return x // w

        if t < 0:
            return False
        d = {}
        w = t + 1
        for i in range(len(nums)):
            m = getID(nums[i], w)
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                d.pop(getID(nums[i - k], w))
        return False


if __name__ == "__main__":
    sol = Solution()
    # nums = [8, 7, 15, 1, 6, 1, 9, 15]
    # k = 1
    # t = 3
    # nums = [1, 2, 3, 1]
    # k = 3
    # t = 0
    nums = [-3, 3, -6]
    k = 2
    t = 3
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums = [1, 0, 1, 1]
    k = 1
    t = 2
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    print("Ans is: ", res)
