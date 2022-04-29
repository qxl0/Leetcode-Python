"""
770. Basic Calculator IV
Hard

116

1193

Add to List

Share
Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]

An expression alternates chunks and symbols, with a space separating each chunk and symbol.
A chunk is either an expression in parentheses, a variable, or a non-negative integer.
A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

For example, expression = "1 + 2 * 3" has an answer of ["7"].
The format of the output is as follows:

For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
For example, we would never write a term like "b*a*c", only "a*b*c".
Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
For example, "a*a*b*c" has degree 4.
The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"].
Terms (including constant terms) with coefficient 0 are not included.
For example, an expression of "0" has an output of [].
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
