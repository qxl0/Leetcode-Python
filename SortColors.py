"""
75. Sort Colors
Medium

9466

408

Add to List

Share
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    nums = [2, 0, 2, 1, 1, 0]
    res = sol.sortColors(nums)
    print(res)
