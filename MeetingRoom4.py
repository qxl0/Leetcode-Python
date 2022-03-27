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

    def max_value2(self, meetings, values):
        meeting_end_time_to_index_value = collections.defaultdict(list)
        last_meeting_ends = 0
        for i in range(len(meetings)):
            meeting_end_time_to_index_value[meetings[i][1]].append(
                (meetings[i][0], values[i])
            )
            last_meeting_ends = max(last_meeting_ends, meetings[i][1])
        dp = [0] * (last_meeting_ends + 1)
        for i in range(1, last_meeting_ends + 1):
            dp[i] = dp[i - 1]
            for j in range(len(meeting_end_time_to_index_value[i])):
                meetinfo = meeting_end_time_to_index_value[i][j]
                start, value = meetinfo
                dp[i] = max(dp[i], dp[start] + value)
        return dp[last_meeting_ends]


if __name__ == "__main__":
    sol = Solution()
    intervals = [[10, 40], [20, 50], [30, 45], [40, 60]]
    value = [3, 6, 2, 4]
    res = sol.max_value2(intervals, value)
    print("result is: ", res)
