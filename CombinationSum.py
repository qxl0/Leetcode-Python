"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)

    def combinationSum2(self, candidates, target):
        res = []
        self.dfs2(candidates, target, [], res)
        return res

    def dfs2(self, candidates, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.dfs2(
                candidates[i:], target - candidates[i], path + [candidates[i]], res
            )

    def combinationSum3(self, nums, target):
        res = []
        nums.sort()

        def dfs(left, path, idx):
            if not left:
                res.append(path[:])
            else:
                for i, val in enumerate(nums[idx:]):
                    if val > left:
                        break
                    dfs(left - val, path + [val], idx + i)

        dfs(target, [], 0)
        return res

    def combinationSum4(self, nums, target):
        result = []
        nums = sorted(nums)

        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return
            for num in nums:
                if num > remain:
                    break
                if stack and num < stack[-1]:
                    continue
                else:
                    dfs(remain - num, stack + [num])

        dfs(target, [])
        return result


class Solution_Backtrack:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(index, cur, remaining):
            if remaining < 0 or index >= len(candidates):
                return
            if remaining == 0:
                output.append(cur.copy())
                return
            cur.append(candidates[index])
            dfs(index, cur, remaining - candidates[index])
            cur.pop()
            dfs(index + 1, cur, remaining)

        dfs(0, [], target)
        return output


if __name__ == "__main__":
    sol = Solution_Backtrack()
    nums = [2, 3, 6, 7]
    target = 7
    res = sol.combinationSum(nums, target)
    print(res)
