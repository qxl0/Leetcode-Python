"""
46. Permutations
Medium

9767

178

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


from typing import List


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if i == len(nums):
                res.append(cur.copy())
            cur.append(i)
            dfs(i + 1, cur)
            cur.pop()

        dfs(0, [])
        return res


if __name__ == "__main__":

    sol = Solution()
    nums = [1, 2, 3]
    res = sol.permute(nums)(nums)
    print(res)
