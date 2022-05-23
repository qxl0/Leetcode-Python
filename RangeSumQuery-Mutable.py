"""
307. Range Sum Query - Mutable
Medium

2751

145

Add to List

Share
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
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
        self.n = len(nums)
        N = self.n

        def buildTree(nums):
            j = 0
            for i in range(N, 2 * N):
                self.tree[i] = nums[j]
                j += 1
            for i in range(N - 1, -1, -1):
                self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

        if N > 0:
            self.tree = [0] * (2 * N)
            buildTree(nums)

    def update(self, index: int, val: int) -> None:
        N = self.n
        index += N
        # update itself
        self.tree[index] = val
        # update parent node
        while index > 0:
            left, right = index, index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        N = self.n
        left += N
        right += N
        sum = 0
        while left <= right:
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    sol = NumArray([-2, 0, 3, -5, 2, -1])
    sol.sumRange(0, 2)
    sol.sumRange(2, 5)
    res = sol.sumRange(0, 5)
    print("Ans is ", res)
