"""
Leetcode 499
The Maze III
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze.
The ball will drop into the hole if it rolls on to the hole.

Given the position of the ball, the position of the hole and the maze, find out how the ball falls into the hole by moving the shortest distance. 
The distance is defined by the number of empty spaces the ball passes from the starting position (excluded) to the hole (included). 
Use "u", "d", "l" and "r" to output the direction of movement. Since there may be several different shortest paths, you should output 
the shortest method in alphabetical order. If the ball doesn't go into the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The ball and the hole coordinates are represented by row and column indexes.
"""
import collections
import heapq
import sys
from typing import (
    List,
)

DIRECTION_HASH = {
    "d": (1, 0),
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
}


class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """

    def find_shortest_way(
        self, maze: List[List[int]], ball: List[int], hole: List[int]
    ) -> str:
        m, n = len(maze), len(maze[0])
        pq = [(0, "", ball[0], ball[1])]
        dist = [[sys.maxsize / 2] * n for _ in range(m)]
        directions = {
            (1, 0): "d",
            (0, -1): "l",
            (0, 1): "r",
            (-1, 0): "u",
        }  # ==> l, u, r, d

        def calcNumOfSteps(x, y, dir_x, dir_y, hole, maze):
            step = 0
            m, n = len(maze), len(maze[0])
            while (
                x + dir_x >= 0
                and x + dir_x < m
                and y + dir_y >= 0
                and y + dir_y < n
                and maze[x + dir_x][y + dir_y] != 1
            ):
                step += 1
                x, y = x + dir_x, y + dir_y
                if x == hole[0] and y == hole[1]:
                    break
            return step

        ret = ""
        while pq:
            d, s, x, y = heapq.heappop(pq)
            if d > dist[x][y]:
                continue
            else:
                dist[x][y] = d
            if x == hole[0] and y == hole[1]:
                ret = s
                break
            for dir_x, dir_y in directions:
                step = calcNumOfSteps(x, y, dir_x, dir_y, hole, maze)
                new_x, new_y = x + dir_x * step, y + dir_y * step
                if d + step >= dist[new_x][new_y]:
                    continue
                heapq.heappush(
                    pq, (d + step, s + directions[(dir_x, dir_y)], new_x, new_y)
                )
        return ret if ret != "" else "impossible"


class MazeGridType:
    SPACE = 0
    WALL = 1


class Solution2:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """

    def findShortestWay(self, maze, ball, hole):
        # corner case check
        if not ball or not hole:
            return "impossible"
        if not maze or not maze[0]:
            return "impossible"

        hole = (hole[0], hole[1])

        # (distance, x, y, path)
        queue = collections.deque([(ball[0], ball[1])])
        distance = {(ball[0], ball[1]): (0, "")}

        while queue:
            x, y = queue.popleft()
            dist, path = distance[(x, y)]

            for direction in DIRECTION_HASH:
                if path and path[-1] == direction:
                    continue

                new_x, new_y = self.kick_ball(x, y, direction, maze, hole)
                new_dist = dist + abs(new_x - x) + abs(new_y - y)
                new_path = path + direction
                if (new_x, new_y) in distance and distance[(new_x, new_y)] <= (
                    new_dist,
                    new_path,
                ):
                    continue

                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = (new_dist, new_path)

        if hole in distance:
            return distance[hole][1]

        return "impossible"

    def kick_ball(self, x, y, direction, maze, hole):
        # kick ball through direction from x, y and return the stopped position
        dx, dy = DIRECTION_HASH[direction]
        while (x, y) != hole and not self.is_wall(x, y, maze):
            x += dx
            y += dy

        if (x, y) == hole:
            return x, y

        return x - dx, y - dy

    def is_wall(self, x, y, maze):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return True
        return maze[x][y] == MazeGridType.WALL


if __name__ == "__main__":
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
    ]
    ball = [4, 3]
    hole = [0, 1]
    # maze = [
    #     [0, 0, 0, 0, 0],
    #     [1, 1, 0, 0, 1],
    #     [0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 1],
    #     [0, 1, 0, 0, 0],
    # ]
    # ball = [0, 0]
    # hole = [3, 3]
    # output "lul"
    sol = Solution2()
    res = sol.findShortestWay(maze, ball, hole)
    print("result is: ", res)
