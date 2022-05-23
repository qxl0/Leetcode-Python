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
        n = len(nums)
        count = [0] * n
        snums = nums.copy()

        def helper(nums, l, r):
            nonlocal count, snums
            if l >= r:
                return

            mid = l + (r - l) // 2

            helper(nums, l, mid)
            helper(nums, mid + 1, r)

            for i in range(l, mid + 1):
                pos = bisect_left(snums, nums[i], mid + 1, r + 1)
                count[i] += pos - (mid + 1)

            snums = snums[:l] + sorted(snums[l : r + 1]) + snums[r + 1 :]
            print(snums)

        helper(nums, 0, n - 1)
        return count


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

        offset = 10**4
        size = 2 * 10**4 + 1
        tree = [0] * 2 * size
        result = []
        for num in nums[::-1]:
            cnt = query(0, num + offset, tree, size)
            result.append(cnt)
            update(num + offset, 1, tree, size)
        return result[::-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 6, 1]
    res = sol.countSmaller(nums)
    print(res)
