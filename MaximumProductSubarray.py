"""
152. Maximum Product Subarray
Medium

11364

350

Add to List

Share
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""
import sys
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = nums[0]
        product2 = nums[0]
        global_p = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], product * nums[i], product2 * nums[i])
            product2 = min(nums[i], product2 * nums[i], product * nums[i])
            product = temp
            global_p = max(global_p, product, product2)
        return global_p


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 3, -2, 4]

    nums = [-4, -3, -2]
    res = s.maxProduct(nums)
    print(res)
