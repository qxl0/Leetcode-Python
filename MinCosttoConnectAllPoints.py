"""
1584. Min Cost to Connect All Points
Medium

1198

46

Add to List

Share
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""


import heapq
from typing import List, Optional


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # cost,pint
        while minH:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res


class Solution2:
    def minCostConnectionPoints(self, points):
        n = len(points)
        Father = [-1 for i in range(n + 1)]
        for i in range(1, n + 1):
            Father[i] = i

        def findFather(x):
            if Father[x] != x:
                Father[x] = findFather(Father[x])
            return Father[x]

        def Union(x, y):
            x = Father[x]
            y = Father[y]
            if x < y:
                Father[y] = x
            else:
                Father[x] = y

        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        count = 0
        ret = 0
        for edge in edges:
            dist, a, b = edge
            if findFather(a) != findFather(b):
                Union(a, b)
                count += 1
                ret += dist
            if count == n - 1:
                break
        return ret


if __name__ == "__main__":
    sol = Solution2()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    res = sol.minCostConnectionPoints(points)
    print(res)
