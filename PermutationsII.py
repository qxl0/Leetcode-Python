"""
47. Permutations II
Medium

4717

90

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""


from typing import List


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":

    sol = Solution()
    nums = [1, 2, 3]
    res = sol.permuteUnique(nums)
    print(res)
