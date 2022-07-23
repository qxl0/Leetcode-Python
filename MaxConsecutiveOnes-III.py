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
            for j in range(0, k + 1):
                if nums[i] == 1:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    if j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 0
                ret = max(ret, dp[i][j])
        print(dp)
        return ret


class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n, ans, l = len(nums), 0, 0
        for r in range(n):
            if nums[r] == 0:
                if k == 0:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    k -= 1
            ans = max(ans, r - l + 1)
            print(l, r, nums[r], k, ans)
        return ans


if __name__ == "__main__":
    sol = Solution2()
    # nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    res = sol.longestOnes(nums, k)
    print(res)
