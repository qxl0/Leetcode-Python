"""
77. Combinations
Medium

3965

133

Add to List

Share
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(level, curr):
            if level == k:
                res.append(curr.copy())
                return
            for i in range(1, n):
                helper(level + 1, curr + [i])

        helper(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 2
    res = sol.combine(n, k)
    print(res)
