"""
1584. Min Cost to Connect All Points
Medium

1198

46

Add to List

Share
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""


from typing import List, Optional


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    res = sol.minCostConnectPoints(points)
    print(res)
