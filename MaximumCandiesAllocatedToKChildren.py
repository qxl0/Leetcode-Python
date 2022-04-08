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
        pass


if __name__ == "__main__":
    sol = Solution()
    candies = [5, 8, 6]
    k = 3
    res = sol.maximumCandies(candies, k)
    print(res)
