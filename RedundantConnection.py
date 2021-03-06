"""
684. Redundant Connection
Medium

3567

286

Add to List

Share
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
"""


import collections
from typing import List


class Solution:
    # exceed time limits
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return False
            parent[px] = py
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]


if __name__ == "__main__":
    sol = Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    res = sol.findRedundantConnection(edges)
    print("result is: ", res)
