from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import functools
from math import inf
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        nums.insert(0, 0)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i]

        ret = 0
        step = 0
        while step < 2:
            for i in range(firstLen, n):
                first = presum[i] - presum[i - firstLen]
                for j in range(i + 1, n - secondLen):
                    second = presum[j + secondLen] - presum[j]
                    ret = max(ret, first + second)
            firstLen, secondLen = secondLen, firstLen
            step += 1
            print(ret)
        return ret


if __name__ == "__main__":
    sol = Solution("a" "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
    firstLen = 4
    secondLen = 3
    res = sol.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(res)
