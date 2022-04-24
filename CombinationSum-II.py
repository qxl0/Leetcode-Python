"""
40. Combination Sum II
Medium

5104

134

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


from re import I
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(avail, path, target):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return
            for i in range(len(avail)):
                if i > 0 and avail[i] == avail[i - 1]:
                    continue
                if avail[i] > target:
                    break
                helper(avail[i + 1 :], path + [avail[i]], target - avail[i])

        candidates.sort()
        helper(candidates, [], target)
        return ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = sol.combinationSum2(candidates, target)
    # res2 = sol.combine2(n, k)
    print(res)
