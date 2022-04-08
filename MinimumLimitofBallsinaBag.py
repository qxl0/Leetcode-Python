"""
1760. Minimum Limit of Balls in a Bag
Medium

923

31

Add to List

Share
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.
"""

from this import d
from typing import List, Optional


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def checkValid(nums, maxOperations, penalty):
            total = 0
            for n in nums:
                total += (n - 1) // penalty
                if total > maxOperations:
                    return False
            return True

        l, r = 1, max(nums)
        minPenalty = r
        while l < r:
            m = l + (r - l) // 2
            if checkValid(nums, maxOperations, m):
                minPenalty = m
                r = m - 1
            else:
                l = m + 1
        return minPenalty


if __name__ == "__main__":
    sol = Solution()
    nums = [9]
    maxOperations = 2
    res = sol.minimumSize(nums, maxOperations)
    print(res)
