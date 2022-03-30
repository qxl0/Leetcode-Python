import math
from typing import List

"""
442. Find All Duplicates in an Array
Medium

Add to List

Share
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each 
integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # What the solution does is that it walks along the list, for each element,
        # it uses the value of that element as index and flip the sign of the number in
        # that index location. From the key hints, since a number
        # can occur once or twice, if the index location is already negative,
        # it means that it was flipped once before, which means this num occurred twice.
        res = []
        for j, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                res.append(num)
            else:
                nums[abs(num) - 1] *= -1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = nums = [4, 3, 2, 7, 8, 2, 3, 1]
    res = s.findDuplicates(nums)
    print(res)
