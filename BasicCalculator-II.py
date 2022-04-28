"""
227. Basic Calculator II
Medium

4233

557

Add to List

Share
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


from math import floor
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "3+2*2"
    res = sol.calculate(s)
    print(res)
