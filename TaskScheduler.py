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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    res = sol.leastInterval(tasks, n)
    print(res)
