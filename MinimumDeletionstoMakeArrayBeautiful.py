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
        pass


if __name__ == "__main__":
    sol = Solution3()
    s = "banana"
    res = sol.longestDupSubstring(s)
    print(res)
