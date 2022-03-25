"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
"""


import collections
import random
from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    res = sol.valid_tree(n, edges)
    print("result is: ", res)
