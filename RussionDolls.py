from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # envelopes.sort(key=lambda x:x[0])

        def lis(nums):
            dp = []

            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)

        nn = [i[1] for i in envelopes]
        print(nn)
        return lis(nn)


if __name__ == "__main__":
    sol = Solution()
    envelopes = [[3, 5], [4, 6], [4, 8], [9, 9]]
    res = sol.maxEnvelopes(envelopes)
    print(res)
