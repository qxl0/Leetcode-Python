import bisect
import sys
from typing import List

"""
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def search2(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # mid and target are on the same side
            isTargetandMidOnSameSide = (nums[mid] - nums[0]) * (target - nums[0]) > 0
            if isTargetandMidOnSameSide:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            elif target > nums[len(nums) - 1]:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] == target else -1

    def search3(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return l if nums[l] == target else -1


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 3, -2, 4]

    # nums = [3, 4, 5, 1, 2]
    # nums = [11, 13, 15, 17]
    # nums = [6, 1, 2, 3, 4, 5]
    # nums = [1, 3, 5]
    # target = 1
    # nums = [1, 3, 5]
    # target = 5
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 1
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    nums = [3, 1]
    target = 1
    res = s.search3(nums, target)
    print(res)
