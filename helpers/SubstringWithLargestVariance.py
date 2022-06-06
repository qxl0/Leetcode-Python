from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1

        def helper(nums):
            n = len(nums)
            dp1 = [0] * n
            dp1[0] = nums[0]

            for i in range(1, n):
                dp1[i] = max(dp1[i - 1] + nums[i], nums[i])
            curSum = 0
            ret = 0
            for i in range(n - 1, -1, -1):
                curSum = max(curSum + nums[i], nums[i])
                if nums[i] == -1:
                    ret = max(ret, dp1[i] + curSum - nums[i])
            return ret

        ret = 0
        for i in range(26):
            for j in range(26):
                if count[i] == 0 or count[j] == 0:
                    continue
                if i == j:
                    continue
                nums = [0] * n
                for k in range(n):
                    if ord(s[k]) == ord("a") + i:
                        nums[k] = 1
                    elif ord(s[k]) == ord("a") + j:
                        nums[k] = -1
                ret = max(ret, helper(nums))
        return ret


if __name__ == "__main__":
    sol = Solution()
    s = "aababbb"
    res = sol.largestVariance(s)
    print(res)
