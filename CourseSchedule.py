"""
207. Course Schedule
Medium

8822

356

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""


from typing import List


class Solution:
    # exceed time limits
    def canFinish(self, numCourses, prerequisites):
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 2
    nums = [[1, 0]]
    res = sol.canFinish(n, nums)
    print("result is: ", res)
