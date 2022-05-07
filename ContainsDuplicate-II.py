"""
219. Contains Duplicate II
Easy

2432

1875

Add to List

Share
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


from math import floor
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - k):
            map = set(nums[i : i + k + 1])
            if len(map) != k + 1:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1, 2, 3]
    k = 3
    res = sol.containsNearbyDuplicate(nums, k)
    print("Ans is: ", res)
