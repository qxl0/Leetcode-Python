"""
66. Plus One
Easy

4019

4072

Add to List

Share
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
 
"""


import collections
import sys
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        temp = digits[::-1]
        for i, v in enumerate(temp):
            carry, newv = divmod(v + carry, 10)
            temp[i] = newv
        if carry:
            temp.append(carry)

        return temp[::-1]


class Solution2:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


if __name__ == "__main__":
    sol = Solution2()
    digits = [1, 2, 8]
    res = sol.plusOne(digits)
    print("Ans is:", res)
    digits = [9, 9, 9]
    res = sol.plusOne(digits)
    print("Ans is:", res)
