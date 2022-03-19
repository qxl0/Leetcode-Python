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
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m  # nums[m] < nums[r], so m might be the one we want
        return min(nums[l], nums[r])


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 3, -2, 4]

    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [3, 4, 5, 1, 2]
    # nums = [11, 13, 15, 17]
    # nums = [6, 1, 2, 3, 4, 5]
    target = 0
    res = s.search(nums, target)
    print(res)
