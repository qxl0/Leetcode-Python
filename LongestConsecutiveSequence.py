"""
128. Longest Consecutive Sequence
Medium

8747

386

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    res = sol.longestConsecutive(nums)
    print("result is: ", res)
