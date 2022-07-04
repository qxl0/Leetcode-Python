"""
407. Trapping Rain Water II
Hard

2702

61

Add to List

Share
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
"""

import collections
import heapq
from math import floor
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        dt = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def neighbors(i, j):
            for di, dj in dt:
                ni, nj = i + di, j + dj
                if m > ni >= 0 and n > nj >= 0:
                    yield (ni, nj)

        q = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(q, (heightMap[i][j], i, j))
        cur = float("-inf")
        ret = 0
        vis = set()
        # print(q)
        while q:
            h, x, y = heapq.heappop(q)
            if (x, y) in vis:
                continue
            vis.add((x, y))
            if cur < h:
                cur = h
            ret += cur - h
            print(f"{x,y}: {ret}")
            for nx, ny in neighbors(x, y):
                if (nx, ny) in vis:
                    continue
                vis.add((nx, ny))
                heapq.heappush(q, (heightMap[nx][ny], nx, ny))
        return ret


if __name__ == "__main__":
    sol = Solution()
    heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    res = sol.trapRainWater(heightMap)
    print("Ans is: ", res)
