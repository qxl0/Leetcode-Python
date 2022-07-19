from collections import Counter
from math import inf
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = [i for i in range(n)]
        print(parent)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if M[i][j] == 1:
                    union(i, j)
        print(parent)
        count = Counter(parent)
        return len(count)


if __name__ == "__main__":
    sol = Solution()
    M = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    res = sol.findCircleNum(M)
    print(res)
