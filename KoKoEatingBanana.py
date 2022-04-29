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

from typing import List, Optional


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkOK(piles, h, speed):
            totalh = 0
            for pile in piles:
                if pile % speed == 0:
                    totalh += pile // speed
                else:
                    totalh += pile // speed + 1
                if totalh > h:
                    return False

            return totalh <= h

        l, r = 1, sum(piles)
        while l < r:
            speed = l + (r - l) // 2
            if checkOK(piles, h, speed):
                r = speed
            else:
                l = speed + 1
        return l

    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        l, r = 0, sum(piles)

        def checkHours(speed):
            h = 0
            for pile in piles:
                if pile % speed == 0:
                    h += pile // speed
                else:
                    h += pile // speed + 1
            return h

        while l < r:
            mid = l + (r - l) // 2
            need = checkHours(mid)
            if need > h:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    sol = Solution()
    # piles = [3, 6, 7, 11]
    # h = 8
    # piles = [30, 11, 23, 4, 20]
    # h = 5
    # piles = [30, 11, 23, 4, 20]
    # h = 5
    piles = [3, 6, 7, 11]
    h = 8
    res = sol.minEatingSpeed2(piles, h)
    print(res)
