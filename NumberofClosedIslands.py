from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            return dfs(i - 1, j) and dfs(i + 1, j) and dfs(i, j - 1) and dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    ans += 1
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
