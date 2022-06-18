"""

"""
import collections
import heapq
import sys
from typing import (
    List,
)


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [
            cell
            for i, row in enumerate(matrix)
            for j, cell in enumerate(row)
            if mi[i] == mx[j]
        ]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[3, 4, 2], [4, 7, 2], [5, 8, 7]]
    res = sol.luckyNumbers(matrix)
    print("result is: ", res)
