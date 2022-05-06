"""
50. Pow(x, n)
Medium

4467

5412

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


from math import floor
from typing import List


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        ans = 1

        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    x = 2.0000
    n = 10
    res = sol.myPow(x, n)
    print(res)
