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


if __name__ == "__main__":
    sol = Solution()
    grid = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
    res = sol.maxKilledEnemies(grid)
    print("result is: ", res)
