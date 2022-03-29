import math
from typing import List

"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            temp1 = [i <= mid for i in nums]
            temp = sum(temp1)
            left, right = [left, mid] if temp > mid else [mid + 1, right]
        return right


if __name__ == "__main__":
    s = Solution2()
    nums = [1, 3, 4, 2, 2]
    # nums = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    # nums = [1, 2, 7, 4, 5, 6, 3, 7, 8, 9]
    res = s.findDuplicate(nums)
    print(res)
