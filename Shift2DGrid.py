from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vector = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                vector.append(grid[i][j])
        # shif k
        vlen = len(vector)
        k = k % vlen
        vector = vector[-k:] + vector[: vlen - k]
        print(vector)
        # conver back
        for i in range(n):
            grid[i // n][i % n] = vector[i]
        return grid


if __name__ == "__main__":
    sol = Solution()
    grid = [[1], [2], [3], [4], [5], [6], [7]]
    k = 23
    res = sol.shiftGrid(grid, 23)
    print(res)
