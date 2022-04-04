"""
167. Two Sum II - Input Array Is Sorted
Medium

5039

909

Add to List

Share
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to 
a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
     def twoSum(self, numbers: List[int], target: int) -> List[int]:


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(nums, target)
    print(res)
