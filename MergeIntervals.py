"""
56. Merge Intervals
Medium

12753

507

Add to List

Share
Given an array of intervals 
where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover 
all the intervals in the input.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = []
        intervals.sort()
        newInterval = intervals[0]
        for _, interval in enumerate(intervals, 1):
            A = newInterval[1] < interval[0]  # newInterval is earlier
            B = interval[1] < newInterval[0]  # newInterval is large (later)
            if A:
                result.append(newInterval)
                newInterval = interval
            elif B:
                result.append(interval)
            elif not A or not B:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        result.append(newInterval)
        return result


if __name__ == "__main__":
    sol = Solution()
    # intervals = [[1, 3], [6, 9]]
    # newInterval = [2, 5]
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    res = sol.merge(intervals)
    print("result is: ", res)
