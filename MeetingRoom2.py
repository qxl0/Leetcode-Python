"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def min_meeting_rooms_ii(self, intervals):
        # Write your code here
        pi = []
        for start, end in intervals:
            pi.append((start, 1))
            pi.append((end, -1))
        pi.sort()
        meeting_room = 0
        ongoing_meeting = 0
        for _, delta in pi:
            ongoing_meeting += delta
            meeting_room = max(meeting_room, ongoing_meeting)

        return meeting_room


if __name__ == "__main__":
    sol = Solution()
    intervals = [(0, 30), (5, 10), (15, 20)]
    res = sol.min_meeting_rooms_ii(intervals)
    print("result is: ", res)
