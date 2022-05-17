from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        m, n = len(grid), len(grid[0])

        def helper(i1, j1, i2, j2):  # (i1,j1)=>(i2,j2)
            val = grid[i1][j1]
            isLeaf = True
            for i in range(i1, i2 + 1):
                if not isLeaf:
                    break
                for j in range(j1, j2 + 1):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
            newNode = None
            if isLeaf:
                newNode = Node(val, True, None, None, None, None)
                return newNode
            else:
                newSize = (i2 - i1 + 1) // 2
                newNode = Node(val, False, None, None, None, None)
                newNode.topLeft = helper(i1, j1, i1 + newSize - 1, j1 + newSize - 1)
                newNode.topRight = helper(i1, j1 + newSize, i1 + newSize - 1, j2)
                newNode.bottomLeft = helper(i1 + newSize, j1, i2, j1 + newSize - 1)
                newNode.bottomRight = helper(i1 + newSize, j1 + newSize, i2, j2)
                return newNode

        return helper(0, 0, m - 1, n - 1)


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1], [1, 0]]
    res = sol.construct(grid)

    print(res)
