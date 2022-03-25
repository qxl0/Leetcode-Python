"""
417. Pacific Atlantic Water Flow
Medium
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west 
if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to 
both the Pacific and Atlantic oceans.
"""


import collections
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        p_visited, a_visited = set(), set()

        def dfs(visited, x, y):
            visited.add((x, y))
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for x_dir, y_dir in directions:
                new_x, new_y = x + x_dir, y + y_dir
                if (
                    0 <= new_x < m
                    and 0 <= new_y < n
                    and heights[new_x][new_y] >= heights[x][y]
                    and (new_x, new_y) not in visited
                ):
                    dfs(visited, new_x, new_y)

        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n - 1)
        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m - 1, j)
        res = list(p_visited.intersection(a_visited))
        return res


if __name__ == "__main__":
    sol = Solution()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    res = sol.pacificAtlantic(heights)
    print("result is: ", res)
