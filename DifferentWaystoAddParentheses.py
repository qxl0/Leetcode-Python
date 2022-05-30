import sys
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        lenexp = len(expression)
        nums = []
        ops = []
        i = 0
        while i < lenexp:
            if expression[i].isdigit():
                num = 0
                while i < lenexp and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                nums.append(num)
            else:
                ops.append(expression[i])
                i += 1
        dp = [[[]] * 21 for _ in range(21)]

        def helper(a, b):
            if len(dp[a][b]) > 0:
                return dp[a][b]
            if a == b:
                dp[a][b].append(nums[a])
                return
            for i in range(a, b):
                helper(a, i)
                helper(i + 1, b)
                for x in dp[a][i]:
                    for y in dp[i + 1][b]:
                        if ops[i] == "+":
                            dp[a][b].append(x + y)
                        elif ops[i] == "-":
                            dp[a][b].append(x - y)
                        elif ops[i] == "*":
                            dp[a][b].append(x * y)

        n = len(nums)
        helper(0, n - 1)
        return dp[0][n - 1]


if __name__ == "__main__":
    sol = Solution()
    s = "2-1-1"
    res = sol.diffWaysToCompute(s)
    print("Ans is: ", res)
