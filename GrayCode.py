"""
89. Gray Code
Medium

1423

2251

Add to List

Share
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
"""


from typing import List, Optional
from helpers.LinkedList import ListNode


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        ret = [0]
        for i in range(1, 2**n):
            ret.append(ret[i - 1] ^ (i & ~(i - 1)))
        return ret


if __name__ == "__main__":
    sol = Solution()
    n = 3
    res = sol.grayCode(n)
    print(res)
