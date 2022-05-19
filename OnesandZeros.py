"""
474. Ones and Zeroes
Medium

2874

324

Add to List

Share
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def getonezero(s):
            one, zero = 0, 0
            for ch in s:
                if ch == "0":
                    zero += 1
                else:
                    one += 1
            return one, zero

        for s in strs:
            one, zero = getonezero(s)
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    res = sol.findMaxForm(strs, m, n)

    print(res)
