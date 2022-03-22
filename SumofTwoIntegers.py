"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
 
"""


from re import I
MAX  =  0b01111111111111111111111111111111
mask = 0b11111111111111111111111111111111
class Solution:
    def getSum(self, a: int, b: int) -> int:

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > 0 else a
    def getSum2(self, a: int, b: int) -> int:
        if b == 0:
          return a if a < MAX else ~(a ^ MAX)

        tmp  = (a ^ b) & mask
        b = ((a & b) << 1) & mask
        a = tmp
        return self.getSum2(a, b)
    def getSum3(self, a, b):
        while b& mask > 0:
            carry = (a&b)<<1
            a = a^b
            b = carry

        return a&mask if b>0 else a
if __name__ == "__main__":
    s = Solution()
    first = 1
    second = MAX
    res = s.getSum(first, second)
    res2 = s.getSum2(first, second)
    print(res, res2)
    x = -1
    y = 1
    res3 = s.getSum3(x, y)
    print(res3)

