from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        next = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
            next[a].append(b)
            next[b].append(a)

        q = [i for i in range(n) if degree[i] == 1]
        count = 0
        vis = set()
        while q:
            qsize = len(q)
            for _ in range(qsize):
                cur = q.pop(0)
                count += 1
                vis.add(cur)
                for nei in next[cur]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
            if count == n - 1 or count == n - 2:
                break

        return [i for i in range(n) if i not in vis]


if __name__ == "__main__":
    sol = Solution()
    # edges = [[1, 0], [1, 2], [1, 3]]
    edges = [[0, 1]]
    n = 2
    res = sol.findMinHeightTrees(n, edges)
    print(res)
