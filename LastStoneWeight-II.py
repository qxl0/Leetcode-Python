from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        # dp[i][j] represents max we can get from stones[:i] with target capacity
        # dp[i][j], put in in knapsack (stones[i-1]+dp[i-1][j-staones[i-1]]) or we dont
        #  dp[i-1][j]
        dp = [[0] * (target + 1) for _ in range(len(stones) + 1)]
        for i in range(1, len(stones) + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= stones[i - 1]:
                    dp[i][j] = max(
                        stones[i - 1] + dp[i - 1][j - stones[i - 1]], dp[i - 1][j]
                    )

        return total - 2 * dp[len(stones)][target]


if __name__ == "__main__":
    sol = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    res = sol.lastStoneWeightII(stones)
    print(res)
