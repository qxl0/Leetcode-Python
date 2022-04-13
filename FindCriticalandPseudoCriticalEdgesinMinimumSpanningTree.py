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


class UnionFindSet:
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


class Solution2:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        edges_index = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges_index.sort(key=lambda x: x[2])

        def find_mst(exl_ege):
            uf = UnionFindSet(n)
            ret = 0
            for i, (u, v, w, _) in enumerate(edges_index):
                if i == exl_ege:
                    continue
                if uf.union(u, v):
                    ret += w
            parent = uf.find(0)
            return ret if all(uf.find(i) == parent for i in range(n)) else sys.maxsize

        def find_mst_with(ege):
            uf = UnionFindSet(n)
            edg_s, edg_e, edg_w, _ = edges_index[ege]
            ret = edg_w
            uf.union(edg_s, edg_e)
            for i, (u, v, w, _) in enumerate(edges_index):
                if i == ege:
                    continue
                if uf.union(u, v):
                    ret += w
            parent = uf.find(0)
            return ret if all(uf.find(i) == parent for i in range(n)) else sys.maxsize

        base = find_mst(-1)
        cri = set()
        p_cri = set()
        for i in range(len(edges_index)):
            res = find_mst(i)
            if res > base:
                cri.add(edges_index[i][3])
            else:
                w = find_mst_with(i)
                if w == base:
                    p_cri.add(edges_index[i][3])
        return [cri, p_cri]


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        # sort edges in asc order based on weight
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        # do not use this edge
        def find_mst_without_this_edge(edge_idx):
            union_find_set = UnionFindSet(n)
            ans = 0
            for i, (u, v, w, _) in enumerate(edges):
                # do not use this edge
                if i == edge_idx:
                    continue
                if union_find_set.union(u, v):
                    ans += w
            parent = union_find_set.find(0)
            return (
                ans
                if all(union_find_set.find(i) == parent for i in range(n))
                else sys.maxsize
            )

        # need to use this edge
        def find_mst_with_this_edge(edge_idx):
            union_find_set = UnionFindSet(n)
            # use this edge first
            u0, v0, w0, _ = edges[edge_idx]
            ans = w0
            union_find_set.union(u0, v0)
            for i, (u, v, w, _) in enumerate(edges):
                # do not use this edge
                if i == edge_idx:
                    continue
                if union_find_set.union(u, v):
                    ans += w
            parent = union_find_set.find(0)
            return (
                ans
                if all(union_find_set.find(i) == parent for i in range(n))
                else sys.maxsize
            )

        # normal MST total weight
        base = find_mst_without_this_edge(-1)
        cri, p_cri = set(), set()
        for i in range(len(edges)):
            wgt_excl = find_mst_without_this_edge(i)
            # if not included, MST total weight would increase
            if wgt_excl > base:
                cri.add(edges[i][3])
            else:
                wgt_incl = find_mst_with_this_edge(i)
                # with this edge, MST total weight doesn't change
                if wgt_incl == base:
                    p_cri.add(edges[i][3])

        return [cri, p_cri]


if __name__ == "__main__":
    sol = Solution2()
    # n = 6
    # edges = [
    #     [0, 1, 1],
    #     [1, 2, 1],
    #     [0, 2, 1],
    #     [2, 3, 4],
    #     [3, 4, 2],
    #     [3, 5, 2],
    #     [4, 5, 2],
    # ]
    n = 6
    edges = [[0, 1, 2], [0, 2, 5], [2, 3, 5], [1, 4, 4], [2, 5, 5], [4, 5, 2]]

    res = sol.findCriticalAndPseudoCriticalEdges(n, edges)
    print("Ans is: ", res)
