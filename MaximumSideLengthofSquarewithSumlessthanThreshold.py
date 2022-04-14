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
        m = len(mat)
        n = len(mat[0])
        presum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # populate presum
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = (
                    presum[i][j - 1]
                    + presum[i - 1][j]
                    + mat[i - 1][j - 1]
                    - presum[i - 1][j - 1]
                )

        def findOK(mid):
            # calculate the sum
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    sum = (
                        presum[i][j]
                        - presum[i][j - mid]
                        - presum[i - mid][j]
                        + presum[i - mid][j - mid]
                    )
                    if sum <= threshold:
                        return True
            return False

        l, r = 0, min(m, n)
        while l < r:
            mid = r - (r - l) // 2
            print(f"{l} - {r}")
            if findOK(mid):
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    s = Solution()
    # mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    # threshold = 4
    mat = [[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]]
    threshold = 40184
    res = s.maxSideLength(mat, threshold)
    print(res)
