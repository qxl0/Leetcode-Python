"""
315. Count of Smaller Numbers After Self
Hard

5536

159

Add to List

Share
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""


from bisect import bisect_left
import collections
from math import floor
from tkinter.tix import Tree
from typing import List

from helpers.TreeNode import TreeNode


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def query(left, right, tree, size):
            # tree: [.....] (20002)
            # return [left,right)
            res = 0
            left += size
            right += size  # leaf
            while left < right:
                if left % 2 == 1:
                    res += tree[left]
                    left += 1
                left //= 2
                if right % 2 == 1:
                    right -= 1
                    res += tree[right]
                right //= 2
            return res

        def update(index, value, tree, size):
            index += size
            tree[index] += value  # add on top of
            # now update parent
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        offset = 10**4
        size = 2 * 10**4 + 1
        tree = [0] * 2 * size
        result = []
        for num in nums[::-1]:
            cnt = query(0, num + offset, tree, size)
            result.append(cnt)
            update(num + offset, 1, tree, size)
        return result[::-1]


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def query(left, right, tree, size):
            # tree: [.....] (20002)
            # return [left,right)
            res = 0
            left += size
            right += size  # leaf
            while left < right:
                if left % 2 == 1:
                    res += tree[left]
                    left += 1
                left //= 2
                if right % 2 == 0:
                    res += tree[right]
                    right -= 1
                right //= 2
            return res

        def update(index, value, tree, size):
            index += size
            tree[index] += value  # add on top of
            # now update parent
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        N = max(nums)
        size = N
        tree = [0] * (2 * size + 2)
        result = []
        for num in nums[::-1]:
            cnt = query(0, num, tree, size)
            result.append(cnt)
            update(num, 1, tree, size)
        return result[::-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 2, 5, 6]
    # nums = [-1, -1]
    res = sol.countSmaller(nums)
    print(res)
