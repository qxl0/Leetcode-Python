from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()
        dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def travelAir(grid, vis, x, y):
            m, n = len(grid), len(grid[0])
            if x == m - 1 and y == n - 1:
                return [(x, y)]
            q = [(x, y)]
            vis.add((x, y))
            res = []
            while q:
                cx, cy = q.pop(0)
                for dx, dy in dt:
                    nx, ny = cx + dx, cy + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if (nx, ny) in vis:
                        continue
                    vis.add((nx, ny))
                    if nx == m - 1 and ny == n - 1:
                        res.append((nx, ny))
                    if grid[nx][ny] == 1:
                        res.append((nx, ny))
                    else:
                        q.append((nx, ny))
            print((x, y), res)
            return res

        q = [(0, 0)]
        vis.add((0, 0))
        step = 0
        while q:
            qsize = len(q)
            for _ in range(qsize):
                x, y = q.pop(0)
                # print(x,y)
                # check its neighbor
                for dx, dy in dt:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if (nx, ny) in vis:
                        continue

                    if grid[nx][ny] == 1:
                        q.append((nx, ny))
                        vis.add((nx, ny))
                    else:
                        for ax, ay in travelAir(grid, vis, nx, ny):
                            if ax == m - 1 and ay == n - 1:
                                return step
                            q.append((ax, ay))
                            vis.add((ax, ay))
            step += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
    res = sol.minimumObstacles(grid)
    print(res)
