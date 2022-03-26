"""
57. Insert Interval
Medium

4530

328

Add to List

Share
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def insert(self, intervals, newInterval):
        pass


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    res = sol.insert(intervals, newInterval)
    print("result is: ", res)
