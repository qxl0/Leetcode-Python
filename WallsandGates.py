from collections import deque
import math

from typing import List

"""
663 · Walls and Gates
Algorithms
Medium
Accepted Rate
56%

DescriptionSolutionNotesDiscussLeaderboard
Description
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
"""


class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        pass


if __name__ == "__main__":
    s = Solution()
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    res = s.walls_and_gates(rooms)
    print(res)
