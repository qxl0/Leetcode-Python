"""
2226. Maximum Candies Allocated to K Children
Medium

271

16

Add to List

Share
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.
"""

from this import d
from typing import List, Optional


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, sum(candies) // k
        while l < r:
            m = l + (r - l + 1) // 2
            print(f"l,r = {l,r}")
            if self.checkValid(candies, k, m):
                l = m
            else:
                r = m - 1
        return l

    def checkValid(self, candies, k, m):
        total = 0
        for candy in candies:
            total += candy // m
            if total >= k:
                return True
        return False

    def maximumCandies2(self, A, k):
        end = sum(candies) // k
        start = 1
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if self.checkValid(candies, k, mid):
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    candies = [5, 8, 6]
    k = 3
    # candies = [4, 7, 5]
    # k = 16
    res = sol.maximumCandies(candies, k)
    print(res)
