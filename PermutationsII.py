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
        res = []

        def dfs(level, avail, curr):
            if level == len(nums):
                res.append(curr)
                return
            for i in range(len(avail)):
                if i > 0 and avail[i] == avail[i - 1]:
                    continue
                dfs(level + 1, avail[:i] + avail[i + 1 :], curr + [avail[i]])

        nums.sort()
        dfs(0, nums, [])
        return res


if __name__ == "__main__":

    sol = Solution()
    nums = [1, 1, 3]
    res = sol.permuteUnique(nums)
    print(res)
