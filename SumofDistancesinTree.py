"""
834. Sum of Distances in Tree
Hard

2532

59

Add to List

Share
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
"""


import collections
from math import floor
from tkinter.tix import Tree
from typing import List

from helpers.TreeNode import TreeNode


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = set()
        res = [0] * n
        cnt = [1] * n

        def dfs(node=0, parent=None):
            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node)
                    cnt[node] += cnt[nei]
                    res[node] += res[nei] + cnt[nei]

        def dfs2(node=0, parent=None):
            for nei in adj[node]:
                if nei != parent:
                    res[nei] = res[node] - cnt[nei] + n - cnt[nei]
                    dfs2(nei, node)

        dfs()
        dfs2()
        return res


if __name__ == "__main__":
    sol = Solution()
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    n = 6
    sol.sumOfDistancesInTree(n, edges)
    print(res)
