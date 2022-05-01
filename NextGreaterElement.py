"""
496. Next Greater Element I
Easy

2710

181

Add to List

Share
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""


from math import floor
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2map = {}
        for i in range(len(nums2)):
            nums2map[nums2[i]] = i

        def findnext(start, val):
            for k in range(start, len(nums2)):
                if nums2[k] > val:
                    return nums2[k]
            return -1

        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2map:
                idx = nums2map[nums1[i]]
                val = findnext(idx + 1, nums1[i])
                ans.append(val)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    res = sol.nextGreaterElement(nums1, nums2)

    print(res)
