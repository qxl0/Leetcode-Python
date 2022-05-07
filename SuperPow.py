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


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int("".join(map(str, b)))
        return pow(a, b, MOD)


class Solution2:
    def superPow(self, a, b):
        curr = a
        ret = 1
        for digit in b[::-1]:
            for i in range(digit):
                ret *= curr
            new_curr = 1
            for i in range(10):
                new_curr *= curr
            curr = new_curr
        return ret


if __name__ == "__main__":
    sol = Solution2()
    a = 2
    b = [1, 0]
    res = sol.superPow(a, b)
    print(res)
