from bisect import bisect, bisect_left
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ret = 0

        def helper(presum, a, b, lower, upper):
            nonlocal ret
            if a >= b:
                return
            mid = a + (b - a) // 2
            helper(presum, a, mid, lower, upper)
            helper(presum, mid + 1, b, lower, upper)
            x, y = 0, 0
            for i in range(a, mid + 1):
                x = bisect_left(presum, presum[i] + lower, mid + 1, b + 1)
                print(presum, mid + 1, b + 1)
                y = bisect(presum, presum[i] + upper, mid + 1, b + 1)
                ret += y - x

            # sort
            i, j = a, mid + 1
            p = 0
            temp = [0] * (b - a + 1)
            while i <= mid and j <= b:
                if presum[i] <= presum[j]:
                    temp[p] = presum[i]
                    i += 1
                else:
                    temp[p] = presum[j]
                    j += 1
                p += 1
            while i <= mid:
                temp[p] = presum[i]
                p += 1
                i += 1
            while j <= b:
                temp[p] = presum[j]
                p += 1
                j += 1
            for i in range(b - a + 1):
                presum[i + a] = temp[i]

        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        helper(presum, 0, n, lower, upper)
        return ret


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    res = sol.countRangeSum(nums, lower, upper)
    print(res)
