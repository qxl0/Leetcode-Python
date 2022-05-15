from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, path, cur):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            path.append(cur)
            grid[i][j] = 0
            dfs(i - 1, j, path, "u")  # up
            dfs(i + 1, j, path, "d")  # down
            dfs(i, j - 1, path, "l")  # left
            dfs(i, j + 1, path, "r")  # right
            path.append("#end")  # back

        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, "start#")
                    ans.add("".join(path))
                    print(ans)
        return len(ans)


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    res = sol.numDistinctIslands(grid)
    print("Ans is: ", res)
