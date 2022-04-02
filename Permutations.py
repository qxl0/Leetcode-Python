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

        def dfs(level, avail, cur):
            if level == len(nums):
                # res.append(cur.copy())
                res.append(cur)
                return
            for i in range(len(avail)):
                dfs(level + 1, avail[:i] + avail[i + 1 :], cur + [avail[i]])

        dfs(0, nums, [])
        return res


if __name__ == "__main__":

    sol = Solution()
    nums = [1, 2, 3]
    res = sol.permute(nums)
    print(res)
