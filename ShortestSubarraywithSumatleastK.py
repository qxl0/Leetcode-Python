"""
862. Shortest Subarray with Sum at Least K
Hard

2891

75

Add to List

Share
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.
"""


import collections
from math import floor
from tkinter.tix import Tree
from typing import List

from helpers.TreeNode import TreeNode


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        psum = [0] * (N + 1)
        for i in range(len(nums)):
            psum[i + 1] = psum[i] + nums[i]
        res = N + 1
        q = collections.deque()
        for i in range(N + 1):
            while q and psum[i] - psum[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and psum[q[-1]] >= psum[i]:
                q.pop()
            q.append(i)
        return res if res <= N else -1


if __name__ == "__main__":
    sol = Solution()
    nums = [2, -1, 2]
    k = 3
    res = sol.shortestSubarray(nums, k)
    print(res)
