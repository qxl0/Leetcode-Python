"""
516. Longest Palindromic Subsequence
Medium

5073

246

Add to List

Share
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s):
        d = {}

        def f(s):
            if s not in d:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i == j else 2 + f(s[i + 1 : j]))
                d[s] = maxL
            return d[s]

        return f(s)


class Solution2:
    def longestPalindromeSubseq(self, s):
        """
        Use DP
        """
        str_len = len(s)
        dp_matrix = [[0] * len(s) for i in range(str_len)]

        k = 0
        while k < str_len:
            for i in range(str_len - k):
                j = i + k
                if i == j:
                    dp_matrix[i][j] = 1
                elif s[i] == s[j]:
                    dp_matrix[i][j] = dp_matrix[i + 1][j - 1] + 2
                else:
                    dp_matrix[i][j] = max(dp_matrix[i][j - 1], dp_matrix[i + 1][j])
            k += 1

        return dp_matrix[0][str_len - 1]


class Solution3:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1] * n
        for j in range(1, len(s)):
            pre = dp[j]
            for i in reversed(range(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]


if __name__ == "__main__":
    sol = Solution3()
    s = "bbbab"
    res = sol.longestPalindromeSubseq(s)
    print(res)
