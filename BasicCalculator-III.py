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
        def compare(a, b):
            map = {"(": -1, "+": 0, "-": 0, "*": 1, "/": 1}
            return map[a] - map[b]

        def operate(nums, ops):
            a, b = nums.pop(), nums.pop()
            op = ops.pop()
            if op == "+":
                return b + a
            elif op == "-":
                return b - a
            elif op == "*":
                return b * a
            elif op == "/":
                return int(b / a)
            else:
                return 0

        nums, ops = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = int(c)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
            elif c == " ":
                continue
            elif c == "(":
                ops.append(c)
            elif c == ")":
                while ops[-1] != "(":
                    nums.append(operate(nums, ops))
                ops.pop()
            else:
                while (
                    ops and compare(c, ops[-1]) <= 0
                ):  # c has lower priority than ops[-1]
                    nums.append(operate(nums, ops))
                ops.append(c)
            i += 1
        while ops:
            nums.append(operate(nums, ops))
        return nums.pop()


if __name__ == "__main__":
    sol = Solution()
    s = "16-4/2"
    res = sol.calculate(s)
    print(res)
