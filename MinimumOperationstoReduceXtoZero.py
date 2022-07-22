from collections import Counter
import heapq
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        presum = [8] * n
        ts = 0
        premap = {}
        for i in range(n):
            ts += nums[i]
            presum[i] = ts
            premap[ts] = i
        ts = 0
        sufsum = [0] * n
        sufmap = {}
        for j in range(len(nums) - 1, -1, -1):
            ts += nums[j]
            sufsum[j] = ts
            sufmap[ts] = j
        # print(presum)
        # print(sufsum)
        ret = float("inf")
        for i in range(n):
            if x - presum[i] in sufmap:
                ret = min(ret, i + n - sufmap[x - presum[i]])
        for j in range(n - 1, -1, -1):
            if x - sufsum[j] in premap:
                ret = min(ret, n - j + premap[x - sufsum[j]])
        return ret if ret != float("inf") else -1


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 20, 1, 1, 3]
    res = sol.minOperations(nums, 10)
    print(res)
