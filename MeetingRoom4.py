"""
Meeting Room 4
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei) and the value of each meeting. You can only attend a meeting at the same time. Please calculate the most value you can get.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def max_value(self, meeting: List[List[int]], value: List[int]) -> int:
        meeting_ends = {}
        last_meeting_end = 0
        for (start, end), val in zip(meeting, value):
            if end not in meeting_ends:
                meeting_ends[end] = []
            meeting_ends[end].append((start, val))
            last_meeting_end = max(last_meeting_end, end)
        dp = [0] * (last_meeting_end + 1)
        for t in range(1, last_meeting_end + 1):
            dp[t] = dp[t - 1]
            if t in meeting_ends:
                for start, val in meeting_ends[t]:
                    dp[t] = max(dp[t], dp[start] + val)
        return dp[last_meeting_end]


if __name__ == "__main__":
    sol = Solution()
    intervals = [[10, 40], [20, 50], [30, 45], [40, 60]]
    value = [3, 6, 2, 4]
    res = sol.max_value(intervals, value)
    print("result is: ", res)
