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
from typing import List, Optional


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minq = []
        for n in nums:
            heapq.heappush(minq, -n)
        for _ in range(k - 1):
            heapq.heappop(minq)

        return -minq[0]


if __name__ == "__main__":
    sol = Solution()
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    res = sol.findKthLargest(nums, k)
    print(res)
