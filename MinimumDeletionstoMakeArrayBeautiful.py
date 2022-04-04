"""
2216. Minimum Deletions to Make Array Beautiful
Medium

234

63

Add to List

Share
You are given a 0-indexed integer array nums. The array nums is beautiful if:

nums.length is even.
nums[i] != nums[i + 1] for all i % 2 == 0.
Note that an empty array is considered beautiful.

You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be 
shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

Return the minimum number of elements to delete from nums to make it beautiful.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if len(res) % 2 == 0 or n != res[-1]:
                res.append(n)
        return len(nums) - (len(res) - len(res) % 2)


class Solution2:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            #
            while j < n and nums[j] == nums[i]:
                j += 1
                res += 1
            if j < n:
                i = j + 1
            else:
                res += 1
                break
        return res


if __name__ == "__main__":
    sol = Solution2()
    # nums = [1, 1, 2, 2, 3, 3]
    nums = [1, 1, 1, 2, 3, 3]
    # nums = [1, 1, 2, 3, 5]
    res = sol.minDeletion(nums)
    print(res)
