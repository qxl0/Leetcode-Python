"""
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
Hard

440

43

Add to List

Share
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] 
represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that 
connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph 
would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.
"""


import sys
from typing import List, Optional
from helpers.TreeNode import TreeNode


class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.size[y] = self.size[x]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    N = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    res = sol.minimumCost(N, connections)
    print("Ans is: ", res)
