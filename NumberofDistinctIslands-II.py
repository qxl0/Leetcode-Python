from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        shapes, vis = set(), set()

        def neighbors(i, j):
            for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    yield (ni, nj)

        def helper(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] != 1 or (r, c) in vis:
                return
            vis.add((r, c))
            shape.append((r, c))
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    helper(nr, nc)

        def canonical(shape):
            res = ""
            xs = [0] * len(shape)
            ys = [0] * len(shape)
            out = [""] * len(shape)
            for c in range(8):
                t = 0
                for x, y in shape:
                    if c <= 1:
                        xs[t] = x
                    elif c <= 3:
                        xs[t] = -x
                    elif c <= 5:
                        xs[t] = y
                    else:
                        xs[t] = -y
                    if c <= 3:
                        if c % 2 == 0:
                            ys[t] = y
                        else:
                            ys[t] = -y
                    else:
                        if c % 2 == 0:
                            ys[t] = x
                        else:
                            ys[t] = -x
                    t += 1

                mx = min(xs)
                my = min(ys)

                for j in range(len(shape)):
                    out[j] = str((xs[j] - mx) * n + (ys[j] - my))

                out.sort()
                candidate = "".join(out)
                if res > candidate:
                    res = candidate
            return res

        for i in range(m):
            for j in range(n):
                shape = []
                helper(i, j)
                if shape:
                    shapes.add(canonical(shape))
        return len(shapes)


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    res = sol.numDistinctIslands2(grid)

    print(res)
