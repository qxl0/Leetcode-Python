"""
The Maze III
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the position of the ball, the position of the hole and the maze, find out how the ball falls into the hole by moving the shortest distance. The distance is defined by the number of empty spaces the ball passes from the starting position (excluded) to the hole (included). Use "u", "d", "l" and "r" to output the direction of movement. Since there may be several different shortest paths, you should output the shortest method in alphabetical order. If the ball doesn't go into the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.
"""
from typing import (
    List,
)


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
        pass


if __name__ == "__main__":
    sol = Solution()
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
    ]
    ball = [4, 3]
    hole = [0, 1]
    res = sol.find_shortest_way(maze, ball, hole)
    print("result is: ", res)
