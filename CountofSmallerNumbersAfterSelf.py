"""
315. Count of Smaller Numbers After Self
Hard

5536

159

Add to List

Share
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""


from bisect import bisect_left
import collections
from math import floor
from tkinter.tix import Tree
from typing import List

from helpers.TreeNode import TreeNode


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n

        def helper(nums, snums, l, r):
            nonlocal count
            if l >= r:
                return

            mid = l + (r - l) // 2

            helper(nums, snums, l, mid)
            helper(nums, snums, mid + 1, r)

            for i in range(l, mid + 1):
                pos = bisect_left(snums, nums[i], mid + 1, r + 1)
                count[i] += pos - (mid + 1)

            snums = snums[:l] + sorted(snums[l : r + 1]) + snums[r + 1 :]

        snums = nums.copy()
        helper(nums, snums, 0, n - 1)
        return count


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 6, 1]
    res = sol.countSmaller(nums)
    print(res)
