"""
1027. Longest Arithmetic Subsequence
Medium

2060

97

Add to List

Share
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 6, 9, 12]
    res = sol.longestArithSeqLength(nums)
    print(res)
