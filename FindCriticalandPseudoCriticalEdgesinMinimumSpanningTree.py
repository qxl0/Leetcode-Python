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
            count = 0
            for u, v, w, i in edges_index:
                if i == exl_ege:
                    continue
                if uf.union(u, v):
                    ret += w
                    count += 1
            parent = uf.find(0)
            return ret if all(uf.find(i) == parent for i in range(n)) else sys.maxsize

        def find_mst_with(ege):
            uf = UnionFindSet(n)
            edg_s, edg_e, edg_w, _ = edges_index[ege]
            ret = edg_w
            uf.union(edg_s, edg_e)
            count = 1
            for u, v, w, i in edges_index:
                if uf.union(u, v):
                    ret += w
                    count += 1
            parent = uf.find(0)
            return ret if all(uf.find(i) == parent for i in range(n)) else sys.maxsize

        base = find_mst(-1)
        cri = set()
        p_cri = set()
        for u, v, w, i in edges_index:
            res = find_mst(i)
            if res > base:
                cri.add(i)
            else:
                w = find_mst_with(i)
                if w == base:
                    p_cri.add(i)
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
    sol = Solution()
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
    # n = 6
    # edges = [[0, 1, 2], [0, 2, 5], [2, 3, 5], [1, 4, 4], [2, 5, 5], [4, 5, 2]]
    n = 14
    edges = [
        [0, 1, 13],
        [0, 2, 6],
        [2, 3, 13],
        [3, 4, 4],
        [0, 5, 11],
        [4, 6, 14],
        [4, 7, 8],
        [2, 8, 6],
        [4, 9, 6],
        [7, 10, 4],
        [5, 11, 3],
        [6, 12, 7],
        [12, 13, 9],
        [7, 13, 2],
        [5, 13, 10],
        [0, 6, 4],
        [2, 7, 3],
        [0, 7, 8],
        [1, 12, 9],
        [10, 12, 11],
        [1, 2, 7],
        [1, 3, 10],
        [3, 10, 6],
        [6, 10, 4],
        [4, 8, 5],
        [1, 13, 4],
        [11, 13, 8],
        [2, 12, 10],
        [5, 8, 1],
        [3, 7, 6],
        [7, 12, 12],
        [1, 7, 9],
        [5, 9, 1],
        [2, 13, 10],
        [10, 11, 4],
        [3, 5, 10],
        [6, 11, 14],
        [5, 12, 3],
        [0, 8, 13],
        [8, 9, 1],
        [3, 6, 8],
        [0, 3, 4],
        [2, 9, 6],
        [0, 11, 4],
        [2, 5, 14],
        [4, 11, 2],
        [7, 11, 11],
        [1, 11, 6],
        [2, 10, 12],
        [0, 13, 4],
        [3, 9, 9],
        [4, 12, 3],
        [6, 7, 10],
        [6, 8, 13],
        [9, 11, 3],
        [1, 6, 2],
        [2, 4, 12],
        [0, 10, 3],
        [3, 12, 1],
        [3, 8, 12],
        [1, 8, 6],
        [8, 13, 2],
        [10, 13, 12],
        [9, 13, 11],
        [2, 11, 14],
        [5, 10, 9],
        [5, 6, 10],
        [2, 6, 9],
        [4, 10, 7],
        [3, 13, 10],
        [4, 13, 3],
        [3, 11, 9],
        [7, 9, 14],
        [6, 9, 5],
        [1, 5, 12],
        [4, 5, 3],
        [11, 12, 3],
        [0, 4, 8],
        [5, 7, 8],
        [9, 12, 13],
        [8, 12, 12],
        [1, 10, 6],
        [1, 9, 9],
        [7, 8, 9],
        [9, 10, 13],
        [8, 11, 3],
        [6, 13, 7],
        [0, 12, 10],
        [1, 4, 8],
        [8, 10, 2],
    ]
    res = sol.findCriticalAndPseudoCriticalEdges(n, edges)
    print("Ans is: ", res)
