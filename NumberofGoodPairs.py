"""
1512. Number of Good Pairs
Easy

2421

141

Add to List

Share
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        ans = 0
        for n in d.values():
            ans += n * (n - 1) / 2
        return int(ans)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    res = sol.numIdenticalPairs(nums)
    print("result is: ", res)
