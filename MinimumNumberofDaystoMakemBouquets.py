"""
1482. Minimum Number of Days to Make m Bouquets
Medium

1623

40

Add to List

Share
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""
from collections import defaultdict, deque
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        def bouquet(day):
            total = 0
            count = 0
            for bday in bloomDay:
                if bday <= day:
                    count += 1
                    if count >= k:
                        total += 1
                        count = 0
                else:
                    count = 0  # reset
            return total

        if n < m * k:
            return -1

        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = l + (r - l) // 2
            if bouquet(mid) >= m:
                r = mid - 1
            else:
                l = mid + 1
        # (r,l)
        return l


if __name__ == "__main__":
    sol = Solution()
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    res = sol.minDays(bloomDay, m, k)

    print(res)
