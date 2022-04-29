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
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
        return sum(stack)


class Solution2:
    def calculate(self, s):
        val, stack, op = 0, [], "+"
        for i, c in enumerate(s):
            if c.isdigit():
                val = val * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(val)
                elif op == "-":
                    stack.append(-val)
                elif op == "*":
                    stack.append(stack.pop() * val)
                elif op == "/":
                    stack.append(int(stack.pop() / val))
                val = 0
                op = c
        return sum(stack)


if __name__ == "__main__":
    sol = Solution2()
    s = "-3-2*2"
    res = sol.calculate(s)
    print(res)
