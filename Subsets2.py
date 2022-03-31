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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i == len(nums):
                # res.append(subset.copy())
                res.append(subset[::])
                return
            # included
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res


class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2]
    res = s.subsetsWithDup(nums)
    print(res)
