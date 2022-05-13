"""
  01 Matrix

Solution
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""


from math import floor
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    res = sol.updateMatrix(mat)

    print(res)
