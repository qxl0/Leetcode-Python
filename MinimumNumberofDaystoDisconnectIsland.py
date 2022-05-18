from collections import defaultdict
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # check if there are >1 islands
        m, n = len(grid), len(grid[0])
        vis = set()
        size = 0
        graph = defaultdict(list)

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

        def mark(grid, prevx, prevy, x, y):
            if grid[x][y] == 0:
                return
            if (prevx, prevy) not in graph[(x, y)]:
                graph[(x, y)].append((prevx, prevy))
            if (x, y) not in graph[(prevx, prevy)]:
                graph[(prevx, prevy)].append((x, y))

        def buildGraph(grid):
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        for ni, nj in neighbors(i, j):
                            mark(grid, i, j, ni, nj)

        def tarjan(parent, cur, time, vis):
            nonlocal timeMap, graph, foundCritialEdge
            vis.add(cur)
            timeMap[cur] = time
            for nei in graph[cur]:
                if nei == parent:
                    continue
                if nei not in vis:
                    tarjan(cur, nei, time + 1, vis)
                if time < timeMap[nei]:
                    foundCritialEdge = True
                timeMap[cur] = min(timeMap[cur], timeMap[nei])

        count = numofislands(grid)
        if count != 1:
            return 0  # already >1 islands
        if size == 1:
            return 1  # 1 island with size 1
        if size == 2:
            return 2  # 1 island with size 2

        buildGraph(grid)
        time = 0
        timeMap = {}
        foundCritialEdge = False
        vis.clear()
        parent, root = None, list(graph.keys())[0]
        tarjan(parent, root, time, vis)
        return 1 if foundCritialEdge else 2


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 0, 0], [0, 1, 1, 0]]
    res = sol.minDays(grid)

    print(res)
