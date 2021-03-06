"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue = [0]
        visited = {}
        while queue:
            node = heapq.heappop(queue)
            visited[node] = True
            for neigh in adj[node]:
                if neigh not in visited:
                    heapq.heappush(queue, neigh)
        return len(visited) == n


class Solution2:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = [i for i in range(n)]

        def find(x):
            xp = uf[x]
            if xp != x:
                uf[x] = find(xp)
            return uf[x]

        def union(x, y):
            uf[x] = y

        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            union(pa, pb)

        return True


if __name__ == "__main__":
    sol = Solution2()
    # n = 5
    # edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    # edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    # n = 5
    # edges = [[1, 0]]
    edges = [[0, 1], [0, 2]]
    n = 3
    res = sol.valid_tree(n, edges)
    print("result is: ", res)
