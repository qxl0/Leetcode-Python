"""
73. Set Matrix Zeroes
Medium

6386

475

Add to List

Share
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


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


class Solution2:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        new_matrix = []
        for j in range(n - 1, -1, -1):
            new_l = []
            for i in range(1, m):
                new_l.append(matrix[i][j])
            new_matrix.append(new_l)
        return matrix.pop(0) + self.spiralOrder(new_matrix)


if __name__ == "__main__":
    sol = Solution2()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    res = sol.spiralOrder(matrix)
    print(res)
