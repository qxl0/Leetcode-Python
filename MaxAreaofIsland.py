"""
133. Clone Graph
Medium

5591

695. Max Area of Island
Medium

5836

146

Add to List

Share
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List

from helpers.Graph import Node


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Ans = 0
        m, n = len(grid), len(grid[0])

        def helper(i, j):

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 0

            return (
                1
                + helper(i + 1, j)
                + helper(i - 1, j)
                + helper(i, j - 1)
                + helper(i, j + 1)
            )

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = helper(i, j)
                    print(f"({i} {j}) : {temp}")
                    Ans = max(Ans, temp)
        return Ans


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dt = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(i, j, area):
            print(f"{i},{j} --- {area}")
            area[0] += 1
            for di, dj in dt:
                ci, cj = i + di, j + dj
                if ci >= 0 and ci < m and cj >= 0 and cj < n and grid[ci][cj] == 1:
                    grid[ci][cj] = 0
                    dfs(ci, cj, area)

        ans = 0
        for i in range(m):
            for j in range(n):
                area = [0]
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j, area)
                    ans = max(ans, area[0])
        return ans


if __name__ == "__main__":
    sol = Solution2()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    res = sol.maxAreaOfIsland(grid)
    print("Ans is: ", res)
