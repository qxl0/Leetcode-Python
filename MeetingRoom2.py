"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def meeting_room_i_i(self, intervals: List[List[int]]):
        pass


if __name__ == "__main__":
    sol = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    res = sol.meeting_room_i_i(intervals)
    print("result is: ", res)
