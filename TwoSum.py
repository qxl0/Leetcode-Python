"""
1. Two Sum
Easy

30836

969

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2index = {}
        for i, v in enumerate(nums):
            remain = target - nums[i]
            if remain in nums2index:
                return [i, nums2index[remain]]
            nums2index[v] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(nums, target)
    print(res)
