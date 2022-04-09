"""
7. Reverse Integer
Medium

6935

9566

Add to List

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

from filecmp import cmp
import math
from typing import List, Optional


class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        r = int(str(x * s)[::-1])
        return s * r * (r < 2**31)


class Solution2:
    def reverse(self, x):
        reverse = 0
        max_int = pow(2, 31) - 1
        min_int = pow(-2, 31)

        while x != 0:
            pop = x % 10 if x >= 0 else (abs(x) % 10) * -1
            x = x // 10 if x >= 0 else math.ceil(x / 10)
            if (reverse > max_int // 10) or (reverse == max_int // 10 and pop > 7):
                return 0
            if (reverse < math.ceil(min_int / 10)) or (
                reverse == math.ceil(min_int / 10) and pop < -8
            ):
                return 0
            reverse = reverse * 10 + pop
        return reverse


if __name__ == "__main__":
    sol = Solution2()
    x = 123
    res = sol.reverse(x)
    print(res)
