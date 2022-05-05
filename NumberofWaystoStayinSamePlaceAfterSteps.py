"""
1269. Number of Ways to Stay in the Same Place After Some Steps
Hard

538

30

Add to List

Share
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.
"""


from math import floor
from typing import List


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = arrLen
        dp = [[0] * (steps // 2 + 2) for _ in range(steps + 1)]
        dp[0][0] = 1

        M = 10**9 + 7
        for k in range(1, steps + 1):
            for i in range(steps // 2 + 1):
                if i == 0:
                    dp[k][i] = (dp[k - 1][i] + dp[k - 1][i + 1]) % M
                elif i == n - 1:
                    dp[k][i] = (dp[k - 1][i - 1] + dp[k - 1][i]) % M
                else:
                    dp[k][i] = (dp[k - 1][i - 1] + dp[k - 1][i] + dp[k - 1][i + 1]) % M
        return dp[steps][0] % M


if __name__ == "__main__":
    sol = Solution()
    steps = 3
    arrLen = 2
    res = sol.numWays(steps, arrLen)
    print(res)
