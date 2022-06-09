from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        pass


if __name__ == "__main__":
    s = Solution()
    x = [2, 1, 1, 2]
    res = s.isSelfCrossing(x)
    print(res)
