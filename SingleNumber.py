"""
136. Single Number
Easy

9562

339

Add to List

Share
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        for k, v in d.items():
            if v == 1:
                return k


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 1, 2, 1, 2]
    res = sol.singleNumber(nums)
    print("result is: ", res)
