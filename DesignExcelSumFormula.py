from collections import Counter
from math import inf
from typing import List


class Excel:
    class Formula:
        def __init__(self, c, v):
            self.cells = c
            self.val = v

    def __init__(self, H: int, W: str):
        self.F = [[None] * (ord(W) - ord("A") + 1) for _ in range(H)]
        self.stack = []

    def set(self, row: int, column: str, val: int) -> None:
        self.F[row - 1][ord(column) - ord("A")] = self.Formula({}, val)
        self.topSort(row - 1, ord(column) - ord("A"))
        self.exec()

    def get(self, row: int, column: str) -> int:
        if not self.F[row - 1][ord(column) - ord("A")]:
            return 0
        return self.F[row - 1][ord(column) - ord("A")].val

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = self.convert(numbers)
        summ = self.calculate_sum(row - 1, ord(column) - ord("A"), cells)
        set(row, column, summ)
        self.F[row - 1][ord(column) - ord("A")] = Formula(cells, summ)
        return summ

    def topSort(self, r, c):
        m, n = len(self.F), len(self.F[0])
        for i in range(m):
            for j in range(n):
                key = chr(ord("A") + c) + str(r + 1)
                if self.F[i][j] and key in self.F[i][j].cells:
                    self.topSort(i, j)
        self.stack.append((r, c))

    def exec(self):
        while self.stack:
            r, c = self.stack.pop()
            if len(self.F[r][c].cells) > 0:
                self.calculate_sum(r, c, self.F[r][c].cells)

    def convert(self, strs):
        res = {}
        for st in strs:
            if st.index(":") < 0:
                res[st] = res.get(st, 0) + 1
            else:
                cells = st.split(":")
                si = int(cells[0][1:])
                ei = int(cells[1][1:])
                sj = cells[0][0]
                ej = cells[1][0]
                for i in range(si, ei + 1):
                    for j in range(sj, ej + 1):
                        key = j + str(i)
                        res[key] = res.get(key, 0) + 1
        return res

    def calculate_sum(self, r, c, cells):
        summ = 0
        for s in cells.keys():
            x = int(s[1:]) - 1
            y = ord(s[0]) - ord("A")
            sum += (self.F[x][y].val if self.F[x][y] else 0) * cells[s]
        self.F[r][c] = self.Formula(cells, summ)
        return summ


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)


if __name__ == "__main__":
    sol = Excel(3, "C")
    sol.set(1, "A", 2)
    sol.sum(3, "C")
    sol.set(3, "C", ["A1", "A1:B2"])
    res = sol.get(3, "C")
    print(res)
