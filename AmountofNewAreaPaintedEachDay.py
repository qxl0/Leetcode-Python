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


from collections import defaultdict
import collections
from math import floor
from typing import List
from sortedcontainers import SortedList


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        posmap = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            posmap[s].append((i, 1))
            posmap[e].append((i, -1))

        s1 = SortedList()
        result = [0] * (len(paint))
        prev = -1
        for pos in sorted(posmap.keys()):
            if s1:
                result[s1[0]] += pos - prev
            prev = pos
            for i, flag in posmap[pos]:
                if flag == 1:
                    s1.add(i)
                else:
                    s1.remove(i)

        return result


if __name__ == "__main__":
    sol = Solution()
    # paint = [[1, 4], [4, 7], [5, 8]]
    paint = [[1, 4], [5, 8], [4, 7]]
    res = sol.amountPainted(paint)

    print(res)
