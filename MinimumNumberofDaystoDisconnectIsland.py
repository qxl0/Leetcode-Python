from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # check if there are >1 islands
        m, n = len(grid), len(grid[0])
        vis = set()
        size = 0

        def numofislands(grid):
            res = 0
            for i in range(m):
                for j in range(n):
                    if (i, j) not in vis and grid[i][j] == 1:
                        res += 1
                        dfs(i, j)
            return res

        def neighbors(i, j):
            for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    yield (ni, nj)

        def dfs(i, j):
            nonlocal size
            if grid[i][j] == 0 or (i, j) in vis:
                return
            size += 1
            vis.add((i, j))
            for ni, nj in neighbors(i, j):
                if grid[ni][nj] == 1 and (ni, nj) not in vis:
                    dfs(ni, nj)

        def buildGraph(grid):
            pass

        def tarjan():
            pass

        count = numofislands(grid)
        if count != 1:
            return 0  # already >1 islands
        if size == 1:
            return 1  # 1 island with size 1
        if size == 2:
            return 2  # 1 island with size 2

        buildGraph(grid)
        tarjan(-1, root, 0, {})


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 1, 0], [0, 1, 1, 0]]
    res = sol.minDays(grid)

    print(res)
