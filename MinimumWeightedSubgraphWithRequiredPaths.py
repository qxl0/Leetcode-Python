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
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 6
    edges = [
        [0, 2, 2],
        [0, 5, 6],
        [1, 0, 3],
        [1, 4, 5],
        [2, 1, 1],
        [2, 3, 3],
        [2, 3, 4],
        [3, 4, 2],
        [4, 5, 1],
    ]
    src1 = 0
    src2 = 1
    dest = 5
    res = sol.minimumWeight(n, edges, src1, src2, dest)
    print(res)
