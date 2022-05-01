"""
1920. Build Array from Permutation
Easy

1196

165

Add to List

Share
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""


from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 2, 1, 5, 3, 4]
    res = sol.buildArray(nums)

    print(res)
