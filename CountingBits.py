"""
 Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""


from re import I
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, len(res)):
            res[i] = self.numberofones(i)
        return res

    def numberofones(self, n):
        counter = 0
        while n > 0:
            counter += 1
            n = n & (n - 1)
        return counter


if __name__ == "__main__":
    s = Solution()
    n = 5
    res3 = s.countBits(n)
    print(res3)
