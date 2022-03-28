"""
73. Set Matrix Zeroes
Medium

6386

475

Add to List

Share
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""
from typing import List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        def setZero(matrix, i, j):
            m, n = len(matrix), len(matrix[0])
            matrix[i] = [0] * n
            for y in range(m):
                matrix[y][j] = 0

        zeroList = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroList.append((i, j))
        for i, j in zeroList:
            setZero(matrix, i, j)


if __name__ == "__main__":
    s = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    res = s.setZeroes(matrix)
    print(matrix)
