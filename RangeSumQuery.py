"""
303. Range Sum Query - Immutable
Easy

1938

1644

Add to List

Share
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = []
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            self.nums.append(t)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    sol = NumArray([-2, 0, 3, -5, 2, -1])
    sol.sumRange(0, 2)
    sol.sumRange(2, 5)
    res = sol.sumRange(0, 5)
    print("Ans is ", res)
