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
        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative
        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch in "+-":
                res += sign * operand
                operand = 0
                if ch == "-":
                    sign = -1
                else:
                    sign = 1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ")":
                res += sign * operand
                res *= stack.pop()  # stack pop 1, sign
                res += stack.pop()  # stack pop 2, operand
                operand = 0
        return res + sign * operand


if __name__ == "__main__":
    sol = Solution()
    # s = "3-(2+(9-4))"
    s = "(1+(4+5+2)-3)+(6+8)"
    res = sol.calculate(s)
    print(res)
