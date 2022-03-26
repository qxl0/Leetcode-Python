"""
Meeting Room III
you have a list intervals of current meetings, and some meeting rooms with start and end timestamp.When a 
stream of new meeting ask coming in, judge one by one whether they can be placed in the current meeting list without overlapping..A meeting room can only hold one meeting at a time. Each inquiry is independent.

The meeting asked can be splited to some times. For example, if you want to ask a meeting for [2, 4], you can split it to [2,3] and [3, 4].
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def meeting_room_i_i_i(
        self, intervals: List[List[int]], rooms: int, ask: List[List[int]]
    ) -> List[bool]:
        pass


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [4, 5], [8, 10]]
    rooms = 1
    ask = [[2, 3], [3, 4]]
    res = sol.meeting_room_i_i_i(intervals)
    print("result is: ", res)
