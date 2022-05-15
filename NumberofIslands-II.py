class Union:
    def __init__(self, N):
        self.parent = [-1 for i in range(N)]

    def setParent(self, x):
        self.parent[x] = x

    def getParent(self, x):
        return self.parent[x]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.parent[px] = py


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        if m <= 0 or n <= 0:
            return ans

        union = Union(m * n)
        dt = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        numofIslands = 0
        for i, j in positions:
            pos = i * n + j
            union.setParent(pos)
            numofIslands += 1
            for di, dj in dt:
                x, y = i + di, j + dj
                curpos = x * n + y
                if x < 0 or x >= m or y < 0 or y >= n or union.getParent(curpos) == -1:
                    continue
                anoIsland = union.find(curpos)
                if pos != anoIsland:
                    union.union(anoIsland, pos)
                    numofIslands -= 1
        ans.append(numofIslands)

        return ans


if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    res = sol.numIslands2(m, n, positions)
    print("Ans is: ", res)
