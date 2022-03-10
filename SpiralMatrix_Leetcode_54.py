class Solution:
  def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

  def spiralOrder2(self, matrix):
    res = []
    while matrix:
      res.extend(matrix.pop(0))
      matrix = [*zip(*matrix)][::-1]
      print("--->", matrix)
    return res

if __name__ == '__main__':
  sol = Solution()
  # matrix = [[1,2,3],[4,5,6],[7,8,9]]
  matrix = [(1,2,3), (4,5,6), (7,8,9)]
  res = sol.spiralOrder2(matrix)
  print(res)