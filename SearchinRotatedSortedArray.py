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
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    res = s.search(nums, target)
    print(res)
