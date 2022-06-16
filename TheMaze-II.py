from typing import List


class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        m, n = len(maze), len(maze[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pq = [(0, start[0], start[1])]
        vis = [[0] * n for _ in range(m)]
        while pq:
            d, x, y = heapq.heappop(pq)
            print(d, " == ", x, y)
            if x == destination[0] and y == destination[1]:
                return d
            if vis[x][y] == 1:
                continue
            vis[x][y] = 1

            # d, 4 dirs
            for dx, dy in dir:
                step = 0
                while m > x + dx >= 0 and n > y + dy >= 0 and maze[x + dx][y + dy] != 1:
                    step += 1
                    x += dx
                    y += dy
                if vis[x][y] == 1:
                    continue
                heapq.heappush(pq, (d + step, x, y))
        return -1


if __name__ == "__main__":
    sol = Solution()
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    start = [0, 4]
    dest = [4, 4]
    res = sol.shortestDistance(maze, start, dest)
    print(res)
