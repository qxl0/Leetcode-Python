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

        def dfs(i):
            pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    res = sol.balanceBST(root)

    print(res)
