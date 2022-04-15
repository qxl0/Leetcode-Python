from collections import deque
import collections
import math

from typing import List

"""
130. Surrounded Regions
Medium

4675

1163

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return

        m, n = len(board), len(board[0])
        save = [
            ij
            for k in range(max(m, n))
            for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))
        ]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "S"
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        board[:] = [["XO"[c == "S"] for c in row] for row in board]


if __name__ == "__main__":
    s = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    res = s.solve(board)
    print("Ans is : ", res)
