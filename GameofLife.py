"""
289. Game of Life
Medium

4708

438

Add to List

Share
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
 
"""


import collections
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Original | New | State
        #    0     |  0  |  0   live nei
        #    1     |  0  |  1   live nei > 3 or < 2
        #    0     |  1  |  2   live nei == 3
        #    1     |  1  |  3   live nei == 2, 3
        m, n = len(board), len(board[0])

        def checkNeigh(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i < 0 or i >= m or j < 0 or j >= n or (i == r and j == c):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for r in range(m):
            for c in range(n):
                nei = checkNeigh(r, c)

                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                    else:
                        board[r][c] = 1
                else:
                    if nei == 3:
                        board[r][c] = 2
        for r in range(m):
            for c in range(n):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
        print(board)


if __name__ == "__main__":
    s = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    res = s.gameOfLife(board)
    print("Ans is:", res)
