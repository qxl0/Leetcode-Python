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
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    res = sol.searchRange(nums)

    print(res)
