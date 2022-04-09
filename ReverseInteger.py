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

from typing import List, Optional


MOD = 2**63 - 1


class Solution:
    def reverse(self, x: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    x = 123
    res = sol.reverse(x)
    print(res)
