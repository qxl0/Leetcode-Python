"""
67. Add Binary
Easy

4857

533

Add to List

Share
Given two binary strings a and b, return their sum as a binary string.
 
"""


import collections
import sys
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry % 2)
            carry //= 2

        return result[::-1]


if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    res = sol.addBinary(a, b)
    print("Ans is:", res)
