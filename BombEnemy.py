from collections import Counter, deque
from heapq import heapify, heappush, heappop


from bisect import bisect, bisect_left
from itertools import zip_longest
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cols = [0] * n
        total = 0
        ans = 0
        for i in range(m):
            rows = 0
            for j in range(n):
                if grid[i][j] == "0":
                    total = rows + cols[j]
                    for k in range(j + 1, n):
                        if grid[i][k] == "W":
                            break
                        if grid[i][k] == "E":
                            total += 1
                    for k in range(i + 1, m):
                        if grid[k][j] == "W":
                            break
                        if grid[k][j] == "E":
                            total += 1
                    ans = max(ans, total)
                elif grid[i][j] == "E":
                    rows += 1
                    cols[j] += 1
                else:
                    rows = 0
                    cols[j] = 0
        return ans

    def maxKilledEnemies2(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        m, n = len(grid), len(grid[0])

        max_count = 0
        row_hits = 0
        col_hits = [0] * n

        for i in range(0, m):
            for j in range(0, n):
                # reset the hits on the row, if necessary.
                if j == 0 or grid[i][j - 1] == "W":
                    row_hits = 0
                    for k in range(j, n):
                        if grid[i][k] == "W":
                            break
                        elif grid[i][k] == "E":
                            row_hits += 1

                if i == 0 or grid[i - 1][j] == "W":
                    col_hits[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == "W":
                            break
                        elif grid[k][j] == "E":
                            col_hits[j] += 1

                # count the hits for each empty cell.
                if grid[i][j] == "0":
                    print(i, j, "row:", row_hits, "col:", col_hits[j])
                    total_hits = row_hits + col_hits[j]
                    max_count = max(max_count, total_hits)

        return max_count


if __name__ == "__main__":
    sol = Solution()
    grid = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
    res = sol.maxKilledEnemies2(grid)
    print("result is: ", res)
