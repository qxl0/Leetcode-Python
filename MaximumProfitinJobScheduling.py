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

        def closest(sorted_dict, key):
            "Return closest key in `sorted_dict` to given `key`."
            if len(sorted_dict) <= 0:
                return -1
            keys = list(islice(sorted_dict.irange(minimum=key), 1))
            keys.extend(islice(sorted_dict.irange(maximum=key, reverse=True), 1))
            return min(keys, key=lambda k: abs(key - k))

        ret = 0
        dp = SortedDict()

        for i in range(0, n):
            cur = ret
            s, e, p = jobs[i]
            pos = closest(dp, s)

            print(dp, ":", s, pos)
            if pos >= 0:
                cur = max(cur, dp[pos] + p)
            else:
                cur = max(cur, p)

            dp[e] = cur
            ret = max(ret, cur)

        return ret


if __name__ == "__main__":
    sol = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    res = sol.jobScheduling(startTime, endTime, profit)
    print(res)
