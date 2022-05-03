"""
463. Island Perimeter
Easy

4322

237

Add to List

Share
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

 
"""


import collections
import heapq
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(grid, i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        def checkPeri(grid, i, j):
            nonlocal ans
            change = 4
            for dx, dy in dt:
                newx, newy = i + dx, j + dy
                if isValid(grid, newx, newy) and grid[newx][newy] != 0:
                    change -= 1
            ans += change
            print(f"{i},{j} --- {change}")

        def helper(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = "-1"
            ans = checkPeri(grid, i, j)
            for dx, dy in dt:
                newx, newy = i + dx, i + dy
                helper(grid, newx, newy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    helper(grid, i, j)
        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    res = sol.islandPerimeter(grid)
    print("result is: ", res)
