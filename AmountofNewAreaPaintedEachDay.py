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
from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        posmap = defaultdict(list)
        for i, p in enumerate(paint):
            # posmap: pos --> (colorid, flag), flag: -1 or 1
            posmap[p[0]].append((i, 1))
            posmap[p[1]].append((i, -1))

        # [(1, [(0, 1)]), (4, [(0, -1), (1, 1)]), (7, [(1, -1)]), (5, [(2, 1)]), (8, [(2, -1)])]
        scanarr = list(posmap.items())
        scanarr.sort(key=lambda x: x[0])
        curpaint = []
        res = [0] * len(paint)
        for i in range(len(scanarr)):
            pos = scanarr[i][0]
            for pid, flag in scanarr[i][1]:
                if flag == 1:  # new paint come in
                    curpaint.append(pid)
                else:
                    curpaint.remove(pid)
            if len(curpaint) > 0:
                res[curpaint[0]] += scanarr[i + 1][0] - pos
        return res


if __name__ == "__main__":
    sol = Solution()
    # paint = [[1, 4], [4, 7], [5, 8]]
    paint = [[1, 4], [5, 8], [4, 7]]
    res = sol.amountPainted(paint)

    print(res)
