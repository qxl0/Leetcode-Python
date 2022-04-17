"""
52. N-Queens II
Hard

1670

209

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
 
"""


import collections
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        def dfs(queens, diff, ssum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q in queens or p - q in diff or p + q in ssum:
                    continue
                dfs(queens + [q], diff + [p - q], ssum + [p + q])

        dfs([], [], [])
        return len(res)


if __name__ == "__main__":
    s = Solution()
    n = 4
    res = s.totalNQueens(n)
    print("Ans is:", res)
