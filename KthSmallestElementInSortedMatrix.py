"""
759. Employee Free Time
Hard

2213. Longest Substring of One Repeating Character
Hard

109

68

Add to List

Share
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def countLessEqual(self, matrix, mid, smaller, larger):

        count, n = 0, len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:

                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1

            else:

                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid

                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def countLess(mid, small, large):
            nonlocal n
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    large = min(large, matrix[row][col])
                    row -= 1
                else:
                    small = max(small, matrix[row][col])
                    count += row + 1
                    col += 1
            return count, small, large

        l, r = matrix[0][0], matrix[n - 1][n - 1]
        while l < r:
            mid = l + (r - l) // 2
            small, large = matrix[0][0], matrix[n - 1][n - 1]
            count, small, large = countLess(mid, small, large)

            if count == k:
                return small
            if count < k:
                l = large
            else:
                r = small
        return l


if __name__ == "__main__":
    sol = Solution2()
    matrix = [[1, 2, 3], [10, 11, 13], [12, 13, 15]]
    k = 8
    res = sol.kthSmallest(matrix, k)

    print(res)
