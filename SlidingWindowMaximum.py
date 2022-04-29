"""
239. Sliding Window Maximum
Hard

9363

330

Add to List

Share
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        d = collections.deque()
        out = []
        for i in range(n):
            while (
                d and nums[d[-1]] < nums[i]
            ):  # new element > q's end, remove it , desc order
                d.pop()
            d.append(i)
            if d[0] == i - k:  # out of sliding window, remove
                d.popleft()
            if i >= k - 1:  # k = 3, i=0,1, no output
                out += [nums[d[0]]]
        return out


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    # nums = [1, -1]
    # k = 1
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # nums = [7, 2, 4]
    # k = 2
    res = sol.maxSlidingWindow(nums, k)
    print(res)
