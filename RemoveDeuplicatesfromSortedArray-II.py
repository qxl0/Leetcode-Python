"""
80. Remove Duplicates from Sorted Array II
Medium

3557

920

Add to List

Share
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        pos = 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] != nums[i + 1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1

    def removeDuplicates2(self, nums):
        if len(nums) < 3:
            return len(nums)
        pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[pos - 2]:
                nums[pos] = nums[i]
                pos += 1
        return pos


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    res = sol.removeDuplicates2(nums)
    print(res)
