import math


class Solution:
    def rotate(self, A):
        n = len(A)
        middle = math.floor(n/2)
        for i in range(middle):
            for j in range(n-middle):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]

if __name__ == '__main__':
  # matrix = [[1,2,3],[4,5,6],[7,8,9]]
  matrix = [[1,2,3,4],[5,6,7,8], [9,11,12,13], [2,5,9,10]]
  s = Solution()
  s.rotate(matrix)
  print(matrix)