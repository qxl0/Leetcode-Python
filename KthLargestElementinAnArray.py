"""
215. Kth Largest Element in an Array
Medium

8842

481

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

from filecmp import cmp
import heapq
import math
import random
from typing import List, Optional


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minq = []
        for n in nums:
            heapq.heappush(minq, -n)
        for _ in range(k - 1):
            heapq.heappop(minq)

        return -minq[0]


class Solution2:
    def fKLQselect(self, nums, k):
        if not nums:
            return
        p = random.choice(nums)
        l, m, r = (
            [x for x in nums if x > p],
            [x for x in nums if x == p],
            [x for x in nums if x < p],
        )
        nums, i, j = l + m + r, len(l), len(l) + len(m)
        return (
            self.fKLQselect(nums[:i], k)
            if k <= i
            else self.fKLQselect(nums[j:], k - j)
            if k > j
            else nums[i]
        )


if __name__ == "__main__":
    sol = Solution2()
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    res = sol.fKLQselect(nums, k)
    print(res)
