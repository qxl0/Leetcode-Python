import sys
from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.data = vec
        self.cur = (0, 0)

    def next(self) -> int:
        i, j = self.cur
        if self.hasNext():
            while not self.data[i][j]:
                self.increase()
            ret = self.data[i][j]
            self.increase()
            return ret

    def increase(self):
        i, j = self.cur
        if j < len(self.data[i]) - 1:
            self.cur = (i, j + 1)
        elif i < len(self.data) - 1:
            self.cur = (i + 1, 0)
        else:
            self.cur = (-1, -1)

    def hasNext(self) -> bool:
        i, j = self.cur
        if i == -1 and j == -1:
            return False
        #
        while i < len(self.data) and len(self.data[i]) == 0:
            i += 1

        if i >= len(self.data):
            return False
        elif j >= len(self.data[i]):
            return False
        return True


if __name__ == "__main__":
    sol = Vector2D([[], [2]])
    res = sol.hasNext()
    res = sol.next()
    res = sol.hasNext()
    print("Ans is: ", res)
