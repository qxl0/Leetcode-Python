matrix = [[1,1,1],[1,0,1],[1,1,1]]
visited = {}
def setRowZero(matrix, i):
    for j in range(len(matrix[0])):
      if matrix[i][j] != 0:
        setIsVisited(matrix, i, j)
        matrix[i][j] = 0
def setColZero(matrix, j):
    for i in range(len(matrix)):
      if matrix[i][j] != 0:
        setIsVisited(matrix, i, j)
        matrix[i][j] = 0
def isVisited(matrix, i, j):
    # return visited.has_key((i,j))
    if (i, j) in visited:
      return True
    return False
def setIsVisited(matrix, i, j):
    visited[(i,j)] = True

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if isVisited(matrix, i, j):
          continue
        if  matrix[i][j] == 0:
            setRowZero(matrix, i)
            setColZero(matrix, j)