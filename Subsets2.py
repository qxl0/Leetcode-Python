import math
from typing import List

"""
90. Subsets II
Medium

4722

147

Add to List

Share
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, path):
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1 :], path + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2]
    res = s.subsets(nums)
    print(res)
