"""
376. Wiggle Subsequence
Medium

2632

93

Add to List

Share
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        up = None
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1] and up != False:
                l += 1
                up = False
            if nums[i] > nums[i - 1] and up != True:
                l += 1
                up = True
        return l


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 7, 4, 9, 2, 5]
    res = sol.wiggleMaxLength(nums)
    print(res)
