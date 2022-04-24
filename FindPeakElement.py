"""
162. Find Peak Element
Medium

5877

3684

Add to List

Share
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
"""


from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """

        def helper(nums, l, r):
            print(f"({l}  {r})")
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return helper(nums, l, mid)
            return helper(nums, mid + 1, r)

        return helper(nums, 0, len(nums) - 1)

    def findPeakElement2(self, nums: List[int]) -> int:
        def helper(nums, l, r):
            print(f"({l} - {r}")
            if l == r:
                return l
            mid = r - (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return helper(nums, l, mid)
            return helper(nums, mid + 1, r)

        return helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 2, 3, 1]
    nums = [1, 2, 1, 3, 5, 6, 4]
    res = sol.findPeakElement2(nums)
    print(res)
