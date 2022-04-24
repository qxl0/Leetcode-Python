"""
179. Largest Number
Medium

4776

403

Add to List

Share
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""


from functools import cmp_to_key
from math import log10
from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Do not return anything, modify nums in-place instead.
        """

        def getSigDigit(n):
            while n >= 10:
                n //= 10
            return n

        def remove_msd(n):
            if n < 10:
                return
            return int(n % (pow(10, log10(n))))

        def comparefn(n1, n2):
            s1 = getSigDigit(n1)
            s2 = getSigDigit(n2)
            if s1 < s2:
                return 1
            elif s1 > s2:
                return -1
            else:
                return comparefn(remove_msd(n1), remove_msd(n2))

        a = sorted(nums, key=cmp_to_key(comparefn))
        print(a)

    def largestNumber2(self, nums):
        def comparefn(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0

        if not any(nums):
            return "0"
        return "".join(sorted(map(str, nums), key=cmp_to_key(comparefn)))

    def largestNumber3(self, nums):
        from functools import cmp_to_key

        def mycmp(x, y):
            return -1 if x + y < y + x else x + y > y + x or 0

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(mycmp), reverse=False)
        return "".join(nums).lstrip("0") or "0"


if __name__ == "__main__":
    sol = Solution()
    # nums = [10, 2]
    # nums = [3, 30]
    nums = [0, 0, 0]
    res = sol.largestNumber3(nums)
    print(res)
