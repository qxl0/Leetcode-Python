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
import sys
from this import d
from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        def getValue(v):
            return matrix[v // n][v % n]

        while l < r:
            mid = l + (r - l) // 2
            val = getValue(mid)
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
        return True if getValue(l) == target else False

    def searchMatrix2(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        def check(k):
            val = matrix[k // n][k % n]
            return val

        l, r = 0, m * n - 1
        while l < r:
            mid = l + (r - l) // 2
            val = check(mid)
            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        return check(l) == target


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    # matrix = [[1, 3, 5, 7], [10, 13, 16, 20], [23, 30, 34, 60]]
    # target = 13
    # matrix = [[1]]
    # target = 0
    res = sol.searchMatrix2(matrix, target)
    print(res)
