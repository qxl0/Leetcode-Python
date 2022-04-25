"""
1940. Longest Common Subsequence Between Sorted Arrays
Medium

93

3

Add to List

Share
Given an array of integer arrays arrays where each arrays[i] is sorted in strictly increasing order, return an integer array representing the longest common subsequence between all the arrays.

A subsequence is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def longestCommonSubsequence(self, arrays):
        pass


if __name__ == "__main__":
    sol = Solution()
    arrays = [[1, 3, 4], [1, 4, 7, 9]]
    res = sol.longestCommonSubsequence(arrays)
    print(res)
