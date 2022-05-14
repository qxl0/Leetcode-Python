"""
1283. Find the Smallest Divisor Given a Threshold
Medium

1394

153

Add to List

Share
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""
from collections import defaultdict, deque
from math import ceil
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n > threshold:
            return float("inf")

        def gettotal(d):
            total = 0
            for n in nums:
                total += ceil(n / d)
            return total

        l, r = 1, max(nums)
        while l <= r:
            print(l, r)
            mid = l + (r - l) // 2
            if gettotal(mid) <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        return r


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 5, 9]
    threshold = 6
    res = sol.smallestDivisor(nums, threshold)

    print(res)
