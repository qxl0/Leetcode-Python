import math
from typing import List

"""
410. Split Array Largest Sum
Hard

5177

134

Add to List

Share
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    nums = [7, 2, 5, 10, 8]
    m = 2
    res = s.splitArray(nums, m)
    print(res)
