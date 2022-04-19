"""
81. Search in Rotated Sorted Array II
Medium

4341

718

Add to List

Share
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and nums[r - 1] == nums[r]:
                r -= 1
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            mid = l + (r - l) // 2
            val = nums[mid]
            if val == target:
                return True
            if val >= nums[l]:
                if val > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # val < nums[l]
                if val < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return True if nums[l] == target else False


if __name__ == "__main__":
    sol = Solution()
    # nums = [2, 5, 6, 0, 0, 1, 2]
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
    target = 2
    res = sol.search(nums, target)
    print(res)
