"""
Meeting Room 
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def meeting_room(self, intervals: List[List[int]]):
        # check there are overlappings
        if not intervals:
            return True
        intervals.sort()  # start time
        cur_start, cur_end = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            A = cur_start >= end
            B = cur_end <= start
            if B:
                cur_start, cur_end = start, end
            elif not A and not B:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    # intervals = [[0, 30], [5, 10], [15, 20]]
    intervals = [[5, 8], [9, 15]]
    res = sol.meeting_room(intervals)
    print("result is: ", res)
