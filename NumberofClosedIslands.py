from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])
        dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            return up and down and left and right

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    ans += 1
        return ans


class Solution2:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        islands += 1

        return islands

    def dfs(self, grid, i, j):
        rows, cols = len(grid), len(grid[0])

        if not (0 <= i < rows and 0 <= j < cols):
            return False

        if grid[i][j] == 1:
            return True

        grid[i][j] = 1

        ans = True
        for r, c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ans &= self.dfs(grid, i + r, j + c)

        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    ]
    res = sol.closedIsland(grid)
    print("Ans is: ", res)
