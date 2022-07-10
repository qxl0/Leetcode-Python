"""

"""

from itertools import islice
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)
        # dp[i]: the maximum profit by end of time i
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])  # sort by endtime

        def find(dp, target):
            l, r = 0, len(dp)
            while l < r:
                m = l + (r - l) // 2
                if dp[m][0] <= target:
                    l = m + 1
                else:
                    r = m
            return l

        dp = [(0, 0)]
        for i in range(0, n):
            s, e, p = jobs[i]
            idx = find(dp, s)
            last = dp[-1][1]
            cur = dp[idx - 1][1] + p
            if cur > last:
                dp.append((e, cur))

        return dp[-1][1]


if __name__ == "__main__":
    sol = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    res = sol.jobScheduling(startTime, endTime, profit)
    print(res)
