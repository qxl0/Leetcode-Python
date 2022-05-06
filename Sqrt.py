"""
69. Sqrt(x)
Easy

3760

3185

Add to List

Share
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""


from math import floor
from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x // 2
        while l <= r:
            m = l + (r - l) // 2
            prod = m * m
            if prod < x:
                l = m + 1
            elif prod > x:
                r = m - 1
            else:
                return m
        return r


if __name__ == "__main__":
    sol = Solution()
    x = 4
    res = sol.mySqrt(x)
    print(res)
