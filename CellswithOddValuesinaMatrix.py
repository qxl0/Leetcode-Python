from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        count = 0
        row = [0] * n
        col = [0] * m
        for x, y in indices:
            row[x] += 1
            col[y] += 1
        print(row)
        print(col)
        for i in range(n):
            for j in range(m):
                if (row[i] + col[j]) % 2 == 1:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    m = 2
    n = 3
    indices = [[0, 1], [1, 1]]
    res = sol.oddCells(m, n, indices)
    print(res)
