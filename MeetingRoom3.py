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
        # (position, is_start, ask_index)
        merged_intervals = []
        for start, end in intervals:
            merged_intervals.append((start, True, -1))
            merged_intervals.append((end, False, -1))
        for index, (start, end) in enumerate(ask):
            merged_intervals.append((start, True, index))
            merged_intervals.append((end, False, index))

        merged_intervals.sort()
        self.meetings = 0
        self.ask_set = set()
        self.result = [True] * len(ask)
        self.rooms = rooms
        for pos, is_start, ask_index in merged_intervals:
            if ask_index == -1:
                self.handle_meeting(is_start)
            else:
                self.handle_ask(is_start, ask_index)

        return self.result

    def handle_meeting(self, is_start):
        if not is_start:
            self.meetings -= 1
            return
        self.meetings += 1
        if self.meetings >= self.rooms:
            self.mark_full()

    def handle_ask(self, is_start, ask_index):
        if is_start:
            if self.meetings >= self.rooms:
                self.result[ask_index] = False
            else:
                self.ask_set.add(ask_index)
        else:
            if ask_index in self.ask_set:
                self.ask_set.remove(ask_index)

    def mark_full(self):
        for index in self.ask_set:
            self.result[index] = False
        self.ask_set.clear()


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [4, 5], [8, 10]]
    rooms = 1
    ask = [[2, 3], [3, 4]]
    res = sol.meeting_room_i_i_i(intervals, rooms, ask)
    print("result is: ", res)
