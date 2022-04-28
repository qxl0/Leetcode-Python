"""
150. Evaluate Reverse Polish Notation
Medium

2943

624

Add to List

Share
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
"""


from math import floor
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                o1 = stack.pop()
                o2 = stack.pop()
                val = int(o1) + int(o2)
                stack.append(val)
            elif t == "-":
                o1 = stack.pop()
                o2 = stack.pop()
                val = int(o2) - int(o1)
                stack.append(val)
            elif t == "*":
                o1 = stack.pop()
                o2 = stack.pop()
                val = int(o1) * int(o2)
                stack.append(val)
            elif t == "/":
                o1 = stack.pop()
                o2 = stack.pop()
                val = int(o2 / o1)
                print(val)
                stack.append(val)
            else:
                stack.append(int(t))
        return stack[-1]


if __name__ == "__main__":
    sol = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    res = sol.evalRPN(tokens)
    print(res)
