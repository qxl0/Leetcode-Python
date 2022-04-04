"""
217. Contains Duplicate
Easy

4263

938

Add to List

Share
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    res = sol.containsDuplicate(nums)
    print(res)
