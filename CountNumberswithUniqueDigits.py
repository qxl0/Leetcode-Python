class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n):
            cur = 9
            base = 9
            for j in range(1, i):
                cur = cur * base
                base -= 1
            dp[i] = dp[i - 1] + cur

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    n = 2
    res = sol.countNumbersWithUniqueDigits(n)
    print("result is: ", res)
