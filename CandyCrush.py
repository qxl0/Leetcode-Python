from collections import Counter
import heapq
from math import inf
from re import I
from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        print("call")
        todo = False
        for i in range(m):
            for j in range(n - 2):
                target = abs(board[i][j])
                if target == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -target
                    todo = True
        for i in range(m - 2):
            for j in range(n):
                target = abs(board[i][j])
                if target == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -target
                    todo = True
        for c in range(n):
            wr = m - 1
            for r in range(m - 1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board


if __name__ == "__main__":
    sol = Solution()
    board = [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014],
    ]
    res = sol.candyCrush(board)
    print(res)
