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


class Solution2:
    def largestVariance(self, s: str) -> int:
        def maxSubArray(nums: List[int]):
            ans = -float("inf")
            runningSum = 0
            seen = False
            for x in nums:
                if x < 0:
                    seen = True
                runningSum += x
                if seen:
                    ans = max(ans, runningSum)
                else:
                    ans = max(ans, runningSum - 1)
                if runningSum < 0:
                    runningSum = 0
                    seen = False
            return ans

        f = set()
        a = ""
        for x in s:
            if x not in f:
                a += x
                f.add(x)

        n = len(s)
        res = 0
        for j in range(len(a) - 1):
            for k in range(j + 1, len(a)):
                x = a[j]
                y = a[k]
                arr = []
                for i in range(n):
                    if s[i] != x and s[i] != y:
                        continue
                    elif s[i] == x:
                        arr.append(1)
                    else:
                        arr.append(-1)

                res = max(res, maxSubArray(arr), maxSubArray([-x for x in arr]))

        return res


if __name__ == "__main__":
    sol = Solution2()
    s = "aababbb"
    res = sol.largestVariance(s)
    print(res)
