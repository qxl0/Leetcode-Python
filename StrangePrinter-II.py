from collections import defaultdict, deque
from typing import List


class Solution:
    def isPrintable(self, T: List[List[int]]) -> bool:
        m, n = len(T), len(T[0])
        adj = defaultdict(set)
        maxColor = max(map(max, T)) + 1
        # print(maxColor)
        left = [n] * maxColor
        right = [-1] * maxColor
        top = [m] * maxColor
        down = [-1] * maxColor

        def paintedby(i, j, color):
            if (
                i >= top[color]
                and i <= down[color]
                and j >= left[color]
                and j <= right[color]
            ):
                return True
            return False

        for i in range(m):
            for j in range(n):
                color = T[i][j]
                left[color] = min(left[color], j)
                right[color] = max(right[color], j)
                top[color] = min(top[color], i)
                down[color] = max(down[color], i)
        for i in range(m):
            for j in range(n):
                for color in range(1, maxColor):
                    if color != T[i][j]:
                        if paintedby(i, j, color):
                            adj[T[i][j]].add(color)
        print(adj)
        vis = [0] * maxColor

        def dfs(cur):
            if vis[cur] == 1:
                return True
            vis[cur] = 2
            for nxt in adj[cur]:
                if vis[nxt] == 1:
                    continue
                if vis[nxt] == 2:
                    return False
                if dfs(nxt) == False:
                    return False
            vis[cur] = 1
            return True

        for i in range(1, maxColor):
            if dfs(i) == False:
                return False
        return True

    def isPrintable2(self, M: List[List[int]]) -> bool:
        m, n = len(M), len(M[0])
        bound = [(61, 61, -1, -1) for i in range(61)]
        for i in range(m):
            for j in range(n):
                color = M[i][j]
                a, b, c, d = bound[color]
                bound[color] = (min(a, i), min(b, j), max(c, i), max(d, j))
        # build graph
        graph = defaultdict(set)
        indegree = [0] * 61
        for color in range(len(bound)):
            a, b, c, d = bound[color]
            if a >= 61:
                continue  # no such color
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    # print(color,i,j)
                    newcolor = M[i][j]
                    if newcolor != color and newcolor not in graph[color]:
                        graph[color].add(newcolor)
                        indegree[newcolor] += 1
        q = deque([i for i in range(61) if indegree[i] == 0])
        # print(q)
        # print(graph)
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return sum(indegree) == 0


if __name__ == "__main__":
    sol = Solution()
    # targetGrid = [[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]
    targetGrid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
    res = sol.isPrintable(targetGrid)
    print(res)
