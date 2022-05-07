"""
372. Super Pow
Medium

469

1091

Add to List

Share
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
"""


from math import floor
from typing import List

MOD = 1337


class DetectSquares:
    def __init__(self):
        pass

    def add(self, point: List[int]) -> None:
        pass

    def count(self, point: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = DetectSquares()
    sol.add([[3, 10]])
    sol.add([[11, 2]])
    sol.add([[3, 2]])
    res = sol.count([[11, 10]])
    print(res)
