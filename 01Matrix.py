"""
  01 Matrix

Solution
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""


from math import floor
import sys
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m == 0:
            return matrix

        dist = [[sys.maxsize / 2] * n for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            i, j = q.pop(0)
            for di, dj in dt:
                newi, newj = i + di, j + dj
                if (
                    newi >= 0
                    and newi < m
                    and newj >= 0
                    and newj < n
                    and dist[newi][newj] > dist[i][j] + 1
                ):
                    dist[newi][newj] = dist[i][j] + 1
                    q.append((newi, newj))
        return dist


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    res = sol.updateMatrix(mat)

    print(res)
