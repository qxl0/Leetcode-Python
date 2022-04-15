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
        indegree = {i: 0 for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        q = collections.deque([c for c in indegree if not indegree[c]])
        result = []
        while q:
            c = q.popleft()
            if c in result:
                continue
            result.append(c)

            for neigh in adj[c]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    q.append(neigh)
        return result if len(result) == numCourses else []


if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    res = sol.findOrder(numCourses, prerequisites)
    print("result is: ", res)
