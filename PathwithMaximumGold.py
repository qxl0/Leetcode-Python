from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import functools
from math import inf
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        vis = set()
        dt = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            ret = 0
            for di, dj in dt:
                ni, nj = i + di, j + dj
                if (ni, nj) in vis:
                    continue
                if ni >= 0 and ni < m and nj >= 0 and nj < n and grid[ni][nj] != 0:
                    vis.add((ni, nj))
                    ret = grid[i][j] + dfs(ni, nj)
                    vis.remove((ni, nj))
            return ret

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ret = max(ret, dfs(i, j))
        return ret


if __name__ == "__main__":
    sol = Solution("a" "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    res = sol.getMaximumGold(grid)
    print(res)
