from collections import Counter
import heapq
from math import inf
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        maxw = max(weights)

        def days2ship(x):
            c = 0
            ship = 0
            for w in weights:
                if ship + w > x:
                    c += 1
                    ship = w
                else:  # ship+x<=x
                    ship += w
            return c + 1

        l, r = maxw, 20  # float("inf")
        while l < r:
            m = l + (r - l) // 2
            d = days2ship(m)
            if d > days:
                l = m + 1
            else:
                r = m
        return l


if __name__ == "__main__":
    sol = Solution()
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    res = sol.shipWithinDays(weights, days)
    print(res)
