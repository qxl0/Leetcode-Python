"""
772. Basic Calculator III
Hard

861

248

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

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
    s = "6-4/2"
    res = sol.calculate(s)
    print(res)
