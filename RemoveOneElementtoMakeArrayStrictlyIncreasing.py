from collections import Counter, deque
from heapq import heapify, heappush, heappop


from bisect import bisect, bisect_left
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        ans = []
        for n in nums:
            pos = bisect_left(ans, n)
            if pos < len(ans):
                ans[pos] = n
            else:
                ans.append(n)
        print(ans)
        return len(ans) >= len(nums) - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 2]
    res = sol.canBeIncreasing(nums)
    print("result is: ", res)
