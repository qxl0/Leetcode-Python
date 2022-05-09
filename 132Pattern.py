"""
456. 132 Pattern
Medium

4513

250

Add to List

Share
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

from math import inf
from this import d
from typing import List, Optional


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_i = inf
        for j in range(len(nums) - 1):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True
        return False


class Solution2:
    def find132Pattern(self, nums):
        stack = []
        curMin = nums[0]

        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and n < stack[-1][0] and stack[-1][1] < n:
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False


if __name__ == "__main__":
    sol = Solution2()
    # nums = [3, 1, 4, 2]
    nums = [6, 12, 3, 4, 6, 11, 20]
    res = sol.find132Pattern(nums)
    print(res)
