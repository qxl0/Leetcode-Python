"""
224. Basic Calculator
Hard

3557

295

Add to List

Share
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


from math import floor
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "-3-2*2"
    res = sol.calculate(s)
    print(res)
