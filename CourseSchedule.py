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


import collections
from typing import List


class Solution:
    # exceed time limits
    def canFinish(self, numCourses, prerequisites):
        # construct adj
        adj = collections.defaultdict(list)
        visited = set()
        res = set()
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(i, adj, visited, res):
            if i in visited:
                return
            visited.add(i)
            if not adj[i]:
                res.add(i)
                return
            for pre in adj[i]:
                dfs(pre, adj, visited, res)
            canDo = all([p in res for p in adj[i]])
            if canDo:
                res.add(i)

        for i in range(n):
            dfs(i, adj, visited, res)
        return len(res) == numCourses

    def canFinish2(self, numCourses, prerequisites):
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not adj[crs]:
                return True
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

    def canFinish3(self, numCourses, prerequisites):
        # similiar to canFinish2, rather use visit[i] == 1 to mean dfs(i) --> True
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish4(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj = collections.defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        starts, visited = [i for i in range(numCourses) if not indegree[i]], set()
        while starts:
            node = starts.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    starts.append(neigh)
        return len(visited) == numCourses

    def canFinish5(self, numCourses, prerequisites):
        indegree = {i: 0 for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}

        for c0, c1 in prerequisites:
            indegree[c0] += 1
            adj[c1].append(c0)

        q = collections.deque([i for i in range(numCourses) if not indegree[i]])
        visited = set()

        while q:
            c = q.popleft()
            if c in visited:
                continue
            visited.add(c)

            for neigh in adj[c]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    q.append(neigh)
        return len(visited) == numCourses


if __name__ == "__main__":
    sol = Solution()
    n = 2
    # nums = [[1, 0], [0, 1]]
    # nums = [[1, 0]]
    # res2 = sol.canFinish4(n, nums)
    # print(res2)
    n = 5
    nums = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    res = sol.canFinish5(n, nums)
    print("result is: ", res)
