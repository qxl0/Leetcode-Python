from collections import Counter
import heapq
from math import inf
from re import I
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 1 if nums[0] == 1 else 0
        if nums[0] == 0:
            dp[0][1] = 1
        ret = 0
        for i in range(1, n):
            for j in range(1, k + 1):
                if nums[i] == 1:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                ret = max(ret, dp[i][j])
        print(dp)
        return ret


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    res = sol.longestOnes(nums, k)
    print(res)
