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
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dsu = DSU(m * n)
        res = 1
        dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in dt:
                        ni, nj = i + di, j + dj
                        if ni < 0 or nj < 0 or ni >= m or nj >= n or grid[ni][nj] != 1:
                            continue
                        dsu.union(i * n + j, ni * n + nj)
                        res = max(res, dsu.size[dsu.find(i * n + j)])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    d = {}
                    for di, dj in dt:
                        ni, nj = i + di, j + dj
                        if ni < 0 or nj < 0 or ni >= m or nj >= n or grid[ni][nj] != 1:
                            continue
                        parent = dsu.find(ni * n + nj)
                        d[parent] = dsu.size[parent]
                    res = max(res, sum(d.values()) + 1)
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [[1, 0], [0, 1]]
    res = sol.largestIsland(nums)

    print(res)
