"""
34. Find First and Last Position of Element in Sorted Array
Medium

10034

284

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


from this import d
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rets = []
        l, r = 0, len(nums) - 1
        # if l == r == 0:
        #     return [-1, -1]
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                r = m
        if l == r and nums[l] == target:
            rets.append(l)
        else:
            rets.append(-1)

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l + 1) // 2  # 0,1 => 0
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m
        if l == r and nums[l] == target:
            rets.append(l)
        else:
            rets.append(-1)

        return rets


if __name__ == "__main__":
    sol = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    nums = []
    target = 0
    res = sol.searchRange(nums, target)

    print(res)
