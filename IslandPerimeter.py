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
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    res = sol.islandPerimeter(grid)
    print("result is: ", res)
