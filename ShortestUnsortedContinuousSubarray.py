from collections import Counter
from math import inf
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        curMax = nums[0]
        r = 0
        for i in range(1, n):
            if nums[i] < curMax:
                r = i
            else:
                curMax = nums[i]
        curMin = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > curMin:
                l = i
            else:
                curMin = nums[i]

        return r - l + 1 if l != r else 0


if __name__ == "__main__":
    sol = Solution()
    for i in ["23590", "9999", "10001"]:
        res = sol.nearestPalindromic(i)
        print(i, res)
