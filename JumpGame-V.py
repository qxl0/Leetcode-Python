"""
1340. Jump Game V
Hard

656

22

Add to List

Share
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.
"""
import collections
import sys
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
    d = 2
    res = s.maxJumps(arr, d)
    print("Ans is : ", res)
