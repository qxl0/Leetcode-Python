"""
74. Search a 2D Matrix
Medium

7137

262

Add to List

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

from statistics import quantiles
from this import d
from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    res = sol.searchMatrix(matrix, target)
    print(res)
