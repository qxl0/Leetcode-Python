"""
973. K Closest Points to Origin
Medium

5336

205

Add to List

Share
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""


import heapq
from math import sqrt
from typing import List, Optional


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minq = []
        for x, y in points:
            dist = sqrt(x * x + y * y)
            heapq.heappush(minq, (dist, [x, y]))

        res = []
        for i in range(k):
            res.append(heapq.heappop(minq)[1])
        return res


if __name__ == "__main__":
    s = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    res = s.kClosest(points, k)
    print("Ans is: ", res)
