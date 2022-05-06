"""
2174. Remove All Ones With Row and Column Flips II
Medium

38

2

Add to List

Share
You are given a 0-indexed m x n binary matrix grid.

In one operation, you can choose any i and j that meet the following conditions:

0 <= i < m
0 <= j < n
grid[i][j] == 1
and change the values of all cells in row i and column j to zero.

Return the minimum number of operations needed to remove all 1's from grid.
 
"""


import collections
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        """
        Do not return anything, modify board in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 1], [1, 1, 1], [0, 1, 0]]
    res = sol.removeOnes(grid)
    print("Ans is:", res)
