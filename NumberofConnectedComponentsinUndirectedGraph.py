"""
Given a a graph of n nodes, and an array of edges where edge[i] = [ai, bi]. 
return the number of connected components in the graph
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def numberofComponents(self, n: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    res = sol.numberofComponents(n, edges)
    print("result is: ", res)
