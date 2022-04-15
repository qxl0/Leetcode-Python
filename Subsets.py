import math
from typing import List

"""
78. Subsets
Medium

9525

153

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, curr):
            print(i, curr)
            if i == len(nums):
                res.append(curr)
                return
            helper(i + 1, curr + [nums[i]])
            helper(i + 1, curr)

        curr = []
        helper(0, curr)
        return res


class Solution2:
    def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        print(nums, path)
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1 :], path + [nums[i]], ret)


if __name__ == "__main__":
    s = Solution()
    # nums = [1, 2, 3]
    nums = [1, 2]
    res = s.subsets(nums)
    print(res)
