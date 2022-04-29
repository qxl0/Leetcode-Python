"""
334. Increasing Triplet Subsequence
Medium

3800

210

Add to List

Share
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float("inf"), float("inf")

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    res = sol.increasingTriplet(nums)
    print(res)
