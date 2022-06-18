"""

"""
import collections
import heapq
import sys
from typing import (
    List,
)


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 4, 3, 0, 4]
    res = sol.specialArray(nums)
    print("result is: ", res)
