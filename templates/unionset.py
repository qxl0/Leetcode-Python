class UnionFind:
    def __init__(self, n):
        self.Father = [i for i in range(n + 1)]

    def findFather(self, x):
        if self.Father[x] != x:
            self.Father[x] = self.findFather(self.Father[x])
        return self.Father[x]

    def Union(self, x, y):
        px, py = self.findFather(x), self.findFather(y)
        if px < py:
            self.Father[py] = px
        else:
            self.Father[px] = py
