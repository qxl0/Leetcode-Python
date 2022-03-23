import sys
from typing import List

"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1."""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize / 2] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != sys.maxsize / 2 else -1


if __name__ == "__main__":
    sol = Solution()
    n = 11
    coins = [1, 2, 5]
    res = sol.coinChange(coins, n)
    print(res)
