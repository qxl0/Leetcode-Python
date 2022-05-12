from collections import deque
import collections
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
        # write your code here
        m = len(rooms)
        n = len(rooms[0])
        visited = set()
        q = collections.deque()

        def addRoom(i, j):
            if (
                i < 0
                or i >= m
                or j < 0
                or j >= n
                or rooms[i][j] == -1
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            q.append((i, j))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = dist

                # add to q
                addRoom(i - 1, j)
                addRoom(i + 1, j)
                addRoom(i, j - 1)
                addRoom(i, j + 1)
            dist += 1


class Solution2:
    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        WALL = -1
        GATE = 0
        EMPTY = 2**31 - 1
        dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = []
        vis = set()

        m, n = len(rooms), len(rooms[0])
        if m == 0:
            return

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:
                    q.append((i, j))

        while q:
            x, y = q.pop(0)

            for dx, dy in dt:
                newx, newy = x + dx, y + dy
                if (
                    newx < 0
                    or newx >= m
                    or newy < 0
                    or newy >= n
                    or rooms[newx][newy] != EMPTY
                ):
                    continue
                rooms[newx][newy] = rooms[x][y] + 1
                q.append((newx, newy))


if __name__ == "__main__":
    s = Solution2()
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    res = s.walls_and_gates(rooms)
    print(rooms)
