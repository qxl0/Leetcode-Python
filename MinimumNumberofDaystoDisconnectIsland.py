from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # check if there are >1 islands
        m, n = len(grid), len(grid[0])
        vis = set()

        def numofislands(grid):
            res = 0
            vis = {}
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
            if grid[i][j] == 0 or (i, j) in vis:
                return
            for ni, nj in neighbors(i, j):
                if (ni, nj) not in vis:
                    vis.add((ni, nj))
                    dfs(ni, nj)

        res = numofislands(grid)
        print(res)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    res = sol.findBottomLeftValue(root)

    print(res)
