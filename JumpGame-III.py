"""
1306. Jump Game III
Medium

2678

66

Add to List

Share
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
"""
import sys
from typing import List


class Solution:
    def canReach(arr, start):
        pass


if __name__ == "__main__":
    s = Solution()
    nums = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    res = s.jump(nums)
    print("Ans is : ", res)
