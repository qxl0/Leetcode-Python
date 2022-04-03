"""
41. First Missing Positive
Hard

9094

1290

Add to List

Share
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

The basic idea is that we have an array with n cells (n is the length of the array). 
If an integer is missing it must be in the range [1..n]. This is the crucial observation we use to deduce the algorithm. 
This means that the range of possible answers is [1..n] if an integer is missing, and if an integer is not missing then the answer is n+1.

I'll try my best to explain why.

Let's picture the only two possibilities:

there is no missing integer in the array
there is a missing integer in the array.
If there is no missing integer, this means that the array has all number from 1 to n. This must mean that the array is full. Why, because in the range [1..n] there are exactly n numbers, and if you place n numbers in an array of length n, the array is by definition full. (in this case solution is to return n+1 which is the first smallest integer).

Once you understand the first case above understanding the second is easy. If there is a missing integer (or more than one), the missing integer(s), let's call it X, must be in the range 1..n. Why, because if the missing integer X is not in the range [1..n] that would imply that all integers [1..n] are in the array, which would mean that the array is full, leaving no space where to place X (since X is not in the range [1..n]).

Then the algorithm becomes:

1- Ignore all numbers <=0 and >n since they are outside the range of possible answers (which we proved was [1..n]). We do this by replacing them with the value n+1.
2- For all other integers <n+1, mark their bucket (cell) to indicate the integer exists. (*see below)
3- Find the first cell not marked, that is the first missing integer. If you did not find an unmarked cell, there was no missing integer, so return n+1.

*I recommend looking at this solution for a very smart way to mark the cells:

https://leetcode.com/problems/first-missing-positive/discuss/17214/Java-simple-solution-with-documentation
"""


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        flags = {}
        for num in nums:
            if num > 0:
                flags[num - 1] = True

        for index in range(len(nums)):
            if index not in flags:
                return index + 1
        return index + 1


if __name__ == "__main__":
    sol = Solution2()
    # nums = [1, 2, 0]  # output: 3
    # nums = [3, 4, -1, 1]  # output: 2
    nums = [7, 8, 9, 11, 12]  # output: 1
    res = sol.firstMissingPositive(nums)
    print(res)
