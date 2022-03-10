class Solution:
  def setZeros(self, matrix):
    rowIndex = 0
    zeroLocated = []
    for row in matrix:
      if 0 not in row:
        rowIndex += 1
        continue
      columnIndex = 0
      for number in row:
        if number == 0:
          zeroLocated.append([rowIndex, columnIndex])
        columnIndex += 1
      rowIndex += 1

    for zero in zeroLocated:
      matrix[zero[0]] = [0] * len(row)
      for row in matrix:
        row[zero[1]] = 0

if __name__ == '__main__':
  m = [[0,1,2,0],[3,4,5,2],[1,2,1,5]]
  # m = [(0,1,2,0),(3,4,5,2),(1,2,1,5)]
  sol = Solution()
  sol.setZeros(m)
  print(m)