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
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        tree = [0] * (2 * n)

        def constructST(st, idx, nums, l, r):
            if l == r:
                st[idx] = nums[l]
                return nums[l]

            mid = l + (r - l) // 2
            st[idx] = constructST(st, 2 * idx, nums, l, mid) + constructST(
                st, 2 * idx + 1, nums, mid + 1, r
            )
            return st[idx]

        constructST(tree, 1, nums, 0, n - 1)
        print(tree)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    res = sol.countRangeSum(nums, lower, upper)
    (0, 5)
    print("Ans is ", res)
