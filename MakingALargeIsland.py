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


class Solution2:
    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {
                        grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1
                    }
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans


if __name__ == "__main__":
    sol = Solution2()
    nums = [[1, 0], [0, 1]]
    res = sol.largestIsland(nums)

    print(res)
