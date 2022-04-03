"""
216. Combination Sum III
Medium

2699

73

Add to List

Share
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def helper(level, avail, curr):
            if level == k and sum(curr) == n:
                res.append(curr)
                return
            for i in range(len(avail)):
                helper(level + 1, avail[i + 1 :], curr + [avail[i]])

        nums = [i for i in range(1, 10)]
        helper(0, nums, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 3
    res = sol.combinationSum3(n, k)
    print(res)
    print(res2)
