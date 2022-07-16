from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for s in range(n, -1, -1):
            for e in range(s, n):
                if s == e:
                    dp[s][e] = nums[s]
                else:
                    a = nums[s] - dp[s + 1][e]
                    b = nums[e] - dp[s][e - 1]
                    dp[s][e] = max(a, b)
        return dp[0][n - 1] >= 0


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 2, 4, 6]
    res = sol.PredictTheWinner(nums)
    print(res)
