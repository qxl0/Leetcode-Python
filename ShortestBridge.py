import collections
from typing import List


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            px, py = py, px

        # px > py
        self.parent[py] = px
        self.size[px] += self.size[py]


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def neighbors(i, j):
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    yield ni, nj

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in vis or grid[i][j] == 0:
                return
            vis.add((i, j))
            q.append((i, j))
            for ni, nj in neighbors(i, j):
                dfs(ni, nj)

        q = collections.deque()
        vis = set()
        found = False
        for i in range(m):
            for j in range(n):
                if not found and grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                curx, cury = q.popleft()
                for nx, ny in neighbors(curx, cury):
                    if grid[nx][ny] == 1:
                        return step
                    q.append((nx, ny))
                    vis.add((nx, ny))
            step += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    res = sol.shortestBridge(grid)

    print(res)
