"""
875. Koko Eating Bananas
Medium

3936

175

Add to List

Share
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

from curses.ascii import SO
from statistics import quantiles
from this import d
from typing import List, Optional


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    res = sol.minEatingSpeed(piles, h)
    print(res)
