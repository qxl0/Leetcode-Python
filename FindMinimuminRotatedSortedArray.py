import bisect
import sys
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return min(nums[l], nums[r])

    def findMin2(self, nums):
        self.__getitem__ = lambda i: nums[i] <= nums[-1]
        return nums[bisect.bisect(self, False, 0, len(nums))]


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 3, -2, 4]

    nums = [3, 1, 2]
    # nums = [3, 4, 5, 1, 2]
    # nums = [11, 13, 15, 17]
    # nums = [6, 1, 2, 3, 4, 5]
    res = s.findMin(nums)
    print(res)
