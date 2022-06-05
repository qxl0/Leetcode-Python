from collections import Counter
import heapq
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n, buildings = (
            len(grid),
            len(grid[0]),
            sum(val for line in grid for val in line if val == 1),
        )
        distSum = [[0] * n for _ in range(m)]
        hit = [[0] * n for _ in range(m)]

        def bfs(startx, starty):
            vis = [[False] * n for k in range(m)]
            vis[startx][starty], count1, q = True, 1, deque([(startx, starty, 0)])

            while q:
                x, y, dist = q.popleft()
                for i, j in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 2)]:
                    if 0 <= i < m and 0 <= j < n and not vis[i][j]:
                        vis[i][j] = True
                        if not grid[i][j]:
                            q.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            print(distSum)
            return count1 == buildings

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    if not bfs(x, y):
                        return -1

        result = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and hit[i][j] == buildings:
                    result = min(result, distSum[i][j])
        return result if result != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    res = sol.shortestDistance(grid)
    print(res)
