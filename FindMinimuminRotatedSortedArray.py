import sys
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = l + (r - l) // 2
        while l < r and m != l:
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
            m = l + (r - l) // 2
        return min(nums[l], nums[r])


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 3, -2, 4]

    # nums = [3, 4, 5, 1, 2]
    nums = [11, 13, 15, 17]
    res = s.findMin(nums)
    print(res)
