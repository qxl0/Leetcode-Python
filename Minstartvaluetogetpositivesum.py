"""
1047. Remove All Adjacent Duplicates In String
Easy

3143

153

Add to List

Share
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 
"""


from math import floor
from string import ascii_lowercase
from typing import List


class Solution:
    def minStartValue(self, nums):
        minstart = 1

        presum = 0
        for num in nums:
            presum += num
            minstart = max(minstart, 1 - presum)

        return minstart


if __name__ == "__main__":
    sol = Solution()
    nums = [-3, 2, -3, 4, 2]
    res = sol.minStartValue(nums)
    print(res)
