from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from math import inf
from re import I
from typing import List
from concurrent.futures import ThreadPoolExecutor
import asyncio


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        m = len(rides)
        rides.insert(0, [0, 0, 0])
        rides.sort(key=lambda x: x[1])
        endpoints = []
        for s, e, p in rides:
            endpoints.append(e)
        # print(endpoints)
        dp = [0] * (m + 1)
        for i in range(1, m + 1):
            dp[i] = dp[i - 1]
            s, e, p = rides[i]
            pos = bisect_right(endpoints, s)
            while endpoints[pos] > s:
                pos -= 1

            # print(pos, endpoints[pos],s)

            dp[i] = max(dp[i], dp[pos] + e - s + p)

        return dp[m]


if __name__ == "__main__":
    sol = Solution()
    n = 10
    rides = [
        [4, 5, 8],
        [3, 6, 6],
        [1, 3, 3],
        [2, 5, 9],
        [4, 9, 5],
        [8, 9, 10],
        [3, 8, 5],
        [3, 5, 2],
        [3, 7, 10],
        [9, 10, 6],
    ]
    res = sol.maxTaxiEarnings(n, rides)
    print(res)
