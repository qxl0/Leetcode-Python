"""
435. Non-overlapping Intervals
Medium

3720

104

Add to List

Share
Given an array of intervals intervals where 
intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    res = sol.eraseOverlapIntervals(intervals)
    print("result is: ", res)
