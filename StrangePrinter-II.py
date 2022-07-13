from collections import defaultdict
from typing import List


class Solution:
    def isPrintable(self, T: List[List[int]]) -> bool:
        m, n = len(T), len(T[0])
        adj = defaultdict(list)
        left = [n] * 61
        right = [-1] * 61
        top = [m] * 61
        down = [-1] * 61

        def paintedby(i, j, color):
            if (
                i >= top[color]
                and i <= down[color]
                and j >= left[color]
                and j <= right[color]
            ):
                return True
            return False

        for i in range(m):
            for j in range(n):
                color = T[i][j]
                left[color] = min(left[color], j)
                right[color] = max(right[color], j)
                top[color] = min(top[color], i)
                down[color] = max(down[color], i)
        for i in range(m):
            for j in range(n):
                for color in range(1, 61):
                    if paintedby(i, j, color):
                        adj[T[i][j]].append(color)
        vis = [0] * 61

        def dfs(cur):
            if vis[cur] == 1:
                return True
            vis[cur] = 2
            for nxt in adj[cur]:
                if vis[nxt] == 1:
                    continue
                if vis[nxt] == 2:
                    return False
                if dfs(nxt) == False:
                    return False
            vis[cur] = 1
            return True

        for i in range(1, 61):
            if dfs(i) == False:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    targetGrid = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]
    res = sol.isPrintable(targetGrid)
    print(res)
