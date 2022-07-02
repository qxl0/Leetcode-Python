from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Father = [i for i in range(n + 1)]

        def findFather(x):
            if Father[x] != x:
                Father[x] = findFather(Father[x])
            return Father[x]

        def Union(x, y):
            px, py = findFather(x), findFather(y)
            if px < py:
                Father[py] = px
            else:
                Father[px] = py

        edges0 = []
        edges1 = []
        edges2 = []

        for t, a, b in edges:
            if t == 3:
                edges0.append([a, b])
            if t == 1:
                edges1.append([a, b])
            if t == 2:
                edges2.append([a, b])

        count0 = 0
        for a, b in edges0:
            if findFather(a) != findFather(b):
                Union(a, b)
                count0 += 1
        Father0 = Father[:]
        count1 = 0
        for a, b in edges1:
            if findFather(a) != findFather(b):
                Union(a, b)
                count1 += 1

        if count0 + count1 != n - 1:
            return -1

        Father = Father0[:]
        count2 = 0
        for a, b in edges2:
            if findFather(a) != findFather(b):
                Union(a, b)
                count2 += 1
        if count0 + count2 != n - 1:
            return -1

        return len(edges) - count0 - count1 - count2


if __name__ == "__main__":
    sol = Solution()
    N = 13
    edges = [
        [1, 1, 2],
        [2, 1, 3],
        [3, 2, 4],
        [3, 2, 5],
        [1, 2, 6],
        [3, 6, 7],
        [3, 7, 8],
        [3, 6, 9],
        [3, 4, 10],
        [2, 3, 11],
        [1, 5, 12],
        [3, 3, 13],
        [2, 1, 10],
        [2, 6, 11],
        [3, 5, 13],
        [1, 9, 12],
        [1, 6, 8],
        [3, 6, 13],
        [2, 1, 4],
        [1, 1, 13],
        [2, 9, 10],
        [2, 1, 6],
        [2, 10, 13],
        [2, 2, 9],
        [3, 4, 12],
        [2, 4, 7],
        [1, 1, 10],
        [1, 3, 7],
        [1, 7, 11],
        [3, 3, 12],
        [2, 4, 8],
        [3, 8, 9],
        [1, 9, 13],
        [2, 4, 10],
        [1, 6, 9],
        [3, 10, 13],
        [1, 7, 10],
        [1, 1, 11],
        [2, 4, 9],
        [3, 5, 11],
        [3, 2, 6],
        [2, 1, 5],
        [2, 5, 11],
        [2, 1, 7],
        [2, 3, 8],
        [2, 8, 9],
        [3, 4, 13],
        [3, 3, 8],
        [3, 3, 11],
        [2, 9, 11],
        [3, 1, 8],
        [2, 1, 8],
        [3, 8, 13],
        [2, 10, 11],
        [3, 1, 5],
        [1, 10, 11],
        [1, 7, 12],
        [2, 3, 5],
        [3, 1, 13],
        [2, 4, 11],
        [2, 3, 9],
        [2, 6, 9],
        [2, 1, 13],
        [3, 1, 12],
        [2, 7, 8],
        [2, 5, 6],
        [3, 1, 9],
        [1, 5, 10],
        [3, 2, 13],
        [2, 3, 6],
        [2, 2, 10],
        [3, 4, 11],
        [1, 4, 13],
        [3, 5, 10],
        [1, 4, 10],
        [1, 1, 8],
        [3, 3, 4],
        [2, 4, 6],
        [2, 7, 11],
        [2, 7, 10],
        [2, 3, 12],
        [3, 7, 11],
        [3, 9, 10],
        [2, 11, 13],
        [1, 1, 12],
        [2, 10, 12],
        [1, 7, 13],
        [1, 4, 11],
        [2, 4, 5],
        [1, 3, 10],
        [2, 12, 13],
        [3, 3, 10],
        [1, 6, 12],
        [3, 6, 10],
        [1, 3, 4],
        [2, 7, 9],
        [1, 3, 11],
        [2, 2, 8],
        [1, 2, 8],
        [1, 11, 13],
        [1, 2, 13],
        [2, 2, 6],
        [1, 4, 6],
        [1, 6, 11],
        [3, 1, 2],
        [1, 1, 3],
        [2, 11, 12],
        [3, 2, 11],
        [1, 9, 10],
        [2, 6, 12],
        [3, 1, 7],
        [1, 4, 9],
        [1, 10, 12],
        [2, 6, 13],
        [2, 2, 12],
        [2, 1, 11],
        [2, 5, 9],
        [1, 3, 8],
        [1, 7, 8],
        [1, 2, 12],
        [1, 5, 11],
        [2, 7, 12],
        [3, 1, 11],
        [3, 9, 12],
        [3, 2, 9],
        [3, 10, 11],
    ]
    res = sol.maxNumEdgesToRemove(N, edges)
    print("Ans is: ", res)
