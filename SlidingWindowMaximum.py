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
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = sol.maxSlidingWindow(nums, k)
    print(res)
