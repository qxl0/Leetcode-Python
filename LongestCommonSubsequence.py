"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0 for j in range(n)] for i in range(m)]
        # dp=[[0 for j in range(len(text2+1))] for i in range(len(text1)+1)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    text1 = "abcde"
    text2 = "ace"
    res = sol.longestCommonSubsequence(text1, text2)
    res2 = sol.longestCommonSubsequence2(text1, text2)
    print("result is:", res, res2)
