"""
476. Number Complement
Easy

1986

105

Add to List

Share
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    num = 5
    res = sol.intervalIntersection(num)
    print(res)
