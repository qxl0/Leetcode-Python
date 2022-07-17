from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(workers), len(bikes)
        dp = {}

        def dist(p0, p1):
            x0, y0 = p0
            x1, y1 = p1
            return abs(x0 - x1) + abs(y0 - y1)

        def dfs(idx, state):
            # print(idx, bin(state),dp)
            if idx == m:
                return 0
            if state in dp:
                return dp[state]

            mm = inf
            for i in range(n):
                # assign bikes[i] to workers[idx]
                if state & (1 << i):
                    continue  # bikes[i] is used
                cur = dist(workers[idx], bikes[i])
                mm = min(mm, cur + dfs(idx + 1, state | 1 << i))
            dp[state] = mm
            return dp[state]

        ret = dfs(0, 0)
        # print(dp)
        return ret


if __name__ == "__main__":
    sol = Solution()
    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    res = sol.assignBikes(workers, bikes)
    print(res)
