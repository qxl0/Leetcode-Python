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

        def helper(level, avail, curr):
            if level == k:
                res.append(curr.copy())
                return
            for i in range(len(avail)):
                helper(level + 1, avail[:i] + avail[i + 1 :], curr + [avail[i]])

        helper(0, [i for i in range(1, n + 1)], [])
        return res

    def combine2(self, n, k):
        sol = []

        def backtrack(remain, comb, nex):
            # solution found
            if remain == 0:
                sol.append(comb.copy())
            else:
                # iterate through all possible candidates
                for i in range(nex, n + 1):
                    # add candidate
                    comb.append(i)
                    # backtrack
                    backtrack(remain - 1, comb, i + 1)
                    # remove candidate
                    comb.pop()

        backtrack(k, [], 1)
        return sol


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 2
    res = sol.combine(n, k)
    res2 = sol.combine2(n, k)
    print(res)
    print(res2)
