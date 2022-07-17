from math import inf
from typing import List


class Solution:
    def smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]]
    ) -> List[int]:
        m, n = len(nums), len(nums[0])
        ans = [[0] * m for _ in range(n + 1)]

        # ans[i][j]: only keeping i digits, j-th smallest number's index in nums
        for j in range(m):
            ans[0][j] = j
        for i in range(1, n + 1):  # trim i
            buckets = {i: [] for i in range(10)}
            for j in range(m):
                idx = ans[i - 1][j]
                c = nums[idx][len(nums[idx]) - i]
                buckets[ord(c) - ord("0")].append(idx)

            j = 0
            for b in range(10):
                for idx in buckets[b]:
                    ans[i][j] = idx
                    j += 1
        rets = []
        for k, trim in queries:
            rets.append(ans[trim][k - 1])
        return rets


if __name__ == "__main__":
    sol = Solution()
    nums = ["102", "473", "251", "814"]
    queries = [[1, 1], [2, 3], [4, 2], [1, 2]]
    res = sol.smallestTrimmedNumbers(nums, queries)
    print(res)
