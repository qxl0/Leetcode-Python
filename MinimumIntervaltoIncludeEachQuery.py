"""
1851. Minimum Interval to Include Each Query
Hard

350

6

Add to List

Share
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
"""


from calendar import c
import collections
import heapq
from math import floor
from typing import List


class Solution:
    def minInterval(self, A, queries):
        A = sorted(A)[::-1]
        h = []
        res = {}
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                if j >= q:
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    res = sol.minInterval(intervals, queries)
    print(res)
