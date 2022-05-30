from math import lcm
import sys
from tkinter import E
from typing import List


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l, r = sys.maxsize

        def count(m, a, b, c):
            return (
                m // a
                + m // b
                + m // c
                - m // lcm(a, b)
                - m // lcm(a, c)
                - m // lcm(b, c)
                + m // lcm(a, b, c)
            )

        while l < r:
            m = l + (r - l) // 2
            if count(m, a, b, c) > n:
                r = m - 1
            else:
                l = m
        return l


if __name__ == "__main__":
    sol = Solution()
    for line in sys.stdin:
        if "q" == line.rstrip():
            break
        n = int(line.rstrip())
        a = 2
        b = 11
        c = 13
        res = sol.nthUglyNumber(n, a, b, c)
        print("Ans is: ", res)
