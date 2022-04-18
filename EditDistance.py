"""
72. Edit Distance
Hard

8173

92

Add to List

Share
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
"""


import collections
import sys
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [list(range(n + 1))] + [[r + 1] + [0] * n for r in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = (
                    dp[i][j]
                    if word1[i] == word2[j]
                    else 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
                )
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    # word1 = "horse"
    # word2 = "ros"
    # word1 = "intention"
    # word2 = "execution"
    word1 = "inten"
    word2 = "execu"
    res = sol.minDistance(word1, word2)
    print("Ans is:", res)
