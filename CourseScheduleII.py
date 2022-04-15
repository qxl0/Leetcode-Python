"""
210. Course Schedule II
Medium

6458

232

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""


import collections
from typing import List


class Solution:
    # exceed time limits
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    res = sol.findOrder(numCourses, prerequisites)
    print("result is: ", res)
