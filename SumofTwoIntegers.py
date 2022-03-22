"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
 
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
            return a & mask if b > 0 else a


if __name__ == "__main__":
    s = Solution()
    a = 3
    b = 2
    res = s.getSum(a, b)
    print(res)
