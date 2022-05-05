"""
759. Employee Free Time
Hard

2158. Amount of New Area Painted Each Day
Hard

89

12

Add to List

Share
There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    paint = [[1, 4], [4, 7], [5, 8]]
    res = sol.amountPaintedkj(paint)

    print(res)
