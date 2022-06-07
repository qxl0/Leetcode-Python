from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1 for i in range(n)]

        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return 0
            else:
                if size[pa] > size[pb]:
                    size[pa] += size[pb]
                    parents[pb] = pa
                else:
                    size[pb] += size[pa]
                    parents[pa] = pb
                return 1

        count = n
        for a, b in edges:
            count -= union(a, b)

        return count


if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    res = sol.countComponents(n, edges)
    print(res)
