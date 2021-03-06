"""
26. Remove Duplicates from Sorted Array
Easy

6380

9928

Add to List

Share
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[x] = nums[i]
                x += 1
        return x


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    nums = [0, 0, 2]
    res = sol.removeDuplicates(nums)
    print(res)
