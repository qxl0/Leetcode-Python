import math

"""
48. Rotate Image
Medium

8558

467

Add to List

Share
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, A):
        n = len(A)
        middle = math.floor(n / 2)
        for i in range(middle):
            for j in range(n - middle):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = (
                    A[~j][i],
                    A[~i][~j],
                    A[j][~i],
                    A[i][j],
                )

    def rotate2(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swap


if __name__ == "__main__":
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 11, 12, 13], [2, 5, 9, 10]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)
