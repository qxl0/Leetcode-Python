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


class Solution:
    def findShortestWay(
        self, maze: List[List[int]], start: List[int], hole: List[int]
    ) -> str:
        m, n = len(maze), len(maze[0])
        hole = tuple(hole)
        dir = [(1, 0, "d"), (-1, 0, "u"), (0, 1, "r"), (0, -1, "l")]

        pq = [(0, start[0], start[1], "")]
        vis = [[0] * n for _ in range(m)]
        while pq:
            d, i, j, path = heapq.heappop(pq)
            print(d, " : ", i, j, path)
            if (i, j) == hole:
                return path
            if vis[i][j] == 1:
                continue
            vis[i][j] = 1

            # d, 4 dirs
            for dx, dy, op in dir:
                x, y, step = i, j, 0
                while m > x + dx >= 0 and n > y + dy >= 0 and maze[x + dx][y + dy] == 0:
                    step += 1
                    x += dx
                    y += dy
                    if (x, y) == hole:
                        break
                if vis[x][y] == 1:
                    continue
                heapq.heappush(pq, (d + step, x, y, path + op))
        return "impossible"


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
