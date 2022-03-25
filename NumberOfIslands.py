"""
200. Number of Islands
Medium

12951

318

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""


import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(grid, x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != "1":
                return
            grid[x][y] = "#"
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dir_x, dir_y in directions:
                new_x, new_y = x + dir_x, y + dir_y
                dfs(grid, new_x, new_y)

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)
        return count


if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "0"],
    ]
    res = sol.numIslands(grid)
    print("result is: ", res)
