"""
372. Super Pow
Medium

469

1091

Add to List

Share
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
"""


from collections import Counter
from math import floor
from typing import List

MOD = 1337


class DetectSquares:
    def __init__(self):
        self.d = Counter()

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for p3, cnt in self.d.items():
            x3, y3 = p3
            if x1 == x3 or abs(x1 - x3) != abs(y1 - y3):
                continue
            ans += cnt * self.d[(x1, y3)] * self.d[(x3, y1)]
        return ans


if __name__ == "__main__":
    sol = DetectSquares()
    sol.add([3, 10])
    sol.add([11, 2])
    sol.add([3, 2])
    res = sol.count([11, 10])
    print(res)
