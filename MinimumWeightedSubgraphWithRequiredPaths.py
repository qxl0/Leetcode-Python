"""
203. Minimum Weighted Subgraph With the Required Paths
Hard

361

11

Add to List

Share
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.
"""

from collections import defaultdict
import heapq
import sys
from typing import List, Optional


class Solution:
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        def dijkstra(src, adj):
            ret = [sys.maxsize / 3 for _ in range(n)]
            visited = set()
            mheap = [(0, src)]
            while mheap:
                w, node = heapq.heappop(mheap)
                if node in visited:
                    continue
                visited.add(node)
                ret[node] = w
                for neigh, neigh_w in adj[node]:
                    heapq.heappush(mheap, (w + neigh_w, neigh))
            return ret

        # preprocess
        adj_list = defaultdict(list)
        rev_adj = defaultdict(list)
        for f, t, w in edges:
            adj_list[f].append((t, w))
            rev_adj[t].append((f, w))

        # find shorted path
        dist2Src1 = dijkstra(src1, adj_list)
        dist2Src2 = dijkstra(src2, adj_list)
        dist2Dest = dijkstra(dest, rev_adj)

        res = sys.maxsize / 3
        for i in range(n):
            res = min(res, dist2Src1[i] + dist2Src2[i] + dist2Dest[i])
        if res == sys.maxsize / 3:
            return -1
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 6
    edges = [
        [0, 2, 2],
        [0, 5, 6],
        [1, 0, 3],
        [1, 4, 5],
        [2, 1, 1],
        [2, 3, 3],
        [2, 3, 4],
        [3, 4, 2],
        [4, 5, 1],
    ]
    src1 = 0
    src2 = 1
    dest = 5
    # n = 3
    # edges = [[0, 1, 1], [2, 1, 1]]
    # src1 = 0
    # src2 = 1
    # dest = 2
    res = sol.minimumWeight(n, edges, src1, src2, dest)
    print(res)
