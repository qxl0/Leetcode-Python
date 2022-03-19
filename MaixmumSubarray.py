import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -sys.maxsize - 1
        global_sum = -sys.maxsize - 1
        for i in range(len(nums)):
            sum = max(nums[i], sum + nums[i])
            global_sum = max(global_sum, sum)
        return global_sum


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = s.maxSubArray(nums)
    print(res)
