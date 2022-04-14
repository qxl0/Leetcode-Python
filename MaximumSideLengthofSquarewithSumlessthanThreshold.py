"""
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Medium

759

59

Add to List

Share
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
 
"""
import sys
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    threshold = 4
    res = s.maxSideLength(mat, threshold)
    print(res)
