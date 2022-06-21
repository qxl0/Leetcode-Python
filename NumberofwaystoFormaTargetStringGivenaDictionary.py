from collections import Counter, deque
from heapq import heapify, heappush, heappop


from bisect import bisect, bisect_left
from itertools import zip_longest
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        m = len(words[0])
        n = len(target)
        h = {}

        for i in range(m):
            tmp = Counter()
            for j in range(len(words)):
                tmp.update(words[j][i])
            h[i + 1] = tmp

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # dp[i][k]: how many ways to form target[:i] using word[:k] note: target[i] not required to be target[i]
        for k in range(m + 1):
            dp[0][k] = 1

        for i in range(1, n + 1):
            for k in range(1, m + 1):
                dp[i][k] = dp[i][k - 1]

                if target[i] in h[i]:
                    dp[i][k] += (dp[i - 1][k - 1] * h[i][target[i]]) % mod
            print(dp)
        return dp[n - 1][m - 1]


if __name__ == "__main__":
    sol = Solution()
    words = ["acca", "bbbb", "caca"]
    target = "aba"
    res = sol.numWays(words, target)
    print("result is: ", res)
