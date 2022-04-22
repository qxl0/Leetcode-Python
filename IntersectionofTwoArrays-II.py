"""
350. Intersection of Two Arrays II
Easy

4317

690

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        nums1.sort()
        nums2.sort()

        i1, i2 = 0, 0
        while i1 < len(nums1) or i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:  # equal
                ret.append(nums1[i1])
                i1 += 1
                i2 += 1
        return ret


if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    res = sol.intersect(nums1, nums2)
    print(res)
