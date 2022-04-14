"""
45. Jump Game II
Medium

7754

289

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, step = len(nums), 0, 0, 0

        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step


if __name__ == "__main__":
    s = Solution()
    # nums = [3, 2, 1, 0, 4]
    nums = [2, 3, 1, 1, 4]
    res = s.jump(nums)
    print("Ans is : ", res)
