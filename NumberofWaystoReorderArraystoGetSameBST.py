"""
1569. Number of Ways to Reorder Array to Get Same BST
Hard

411

44

Add to List

Share
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.pascalTriangle = [[1] * 1000 for _ in range(1000)]
        self.buildPascalTriangle()

    def buildPascalTriangle(self):
        n = 1000
        p = self.pascalTriangle
        for i in range(n):
            p[i][0] = p[i][-1] = 1
        for i in range(2, n):
            for j in range(1, i):
                p[i][j] = p[i - 1][j - 1] + p[i - 1][j]

    def numOfWays(self, nums: List[int]) -> int:
        def combine(n, k):
            return self.pascalTriangle[n][k]

        def partition(nums, root):
            left = [i for i in nums if i < root]
            right = [i for i in nums if i > root]
            return left, right

        if len(nums) <= 2:
            return 1
        root = nums[0]
        left, right = partition(nums, root)
        total = (
            combine(len(left) + len(right), len(left))
        ) % self.MOD * self.numOfWays(left) * self.numOfWays(right) - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 5, 1, 2]
    res = sol.numOfWays(nums)

    print(res)
