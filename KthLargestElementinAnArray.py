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
import math
from typing import List, Optional


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    res = sol.findKthLargest(nums, k)
    print(res)
