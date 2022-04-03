"""
43. Multiply Strings
Medium

4230

1663

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i1 in range(len(num1)):
            digit1 = int(num1[i1])
            for i2 in range(len(num2)):
                digit2 = int(num2[i2])
                digit = digit1 * digit2
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    num1 = "2"
    num2 = "3"
    res = sol.multiply(num1, num2)
    print(res)
