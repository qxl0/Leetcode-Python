"""
1135. Connecting Cities with Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

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
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # connections = sorted(connections, key=lambda x: x[2])
        connections.sort(key=lambda x: x[2])
        res = 0
        count = 0
        uf = UnionFind(N)
        for u, v, cost in connections:
            if uf.union(u - 1, v - 1):
                res += cost
                count += 1
        if count == N - 1:
            return res

        return -1


if __name__ == "__main__":
    sol = Solution()
    N = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    res = sol.minimumCost(N, connections)
    print("Ans is: ", res)
