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


if __name__ == "__main__":
    sol = Solution()
    a = 2
    b = [1, 0]
    res = sol.superPow(a, b)
    print(res)
