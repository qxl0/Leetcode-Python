"""
628. Maximum Product of Three Numbers
Easy

2678

524

Add to List

Share
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""
import sys
from typing import List


class Solution:
    def maximumProduct(self, nums):
        max1, max2, max3 = -float("inf"), -float("inf"), -float("inf")
        min1, min2 = float("inf"), float("inf")

        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        return max(max1 * max2 * max3, max1 * min1 * min2)


if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 2, 1]
    res = s.maximumProduct(nums)
    print(res)
