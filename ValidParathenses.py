"""
20. Valid Parentheses
Easy

12329

540

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s):
        d = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0


class Solution2:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
            if l == len(s):
                return False
        return True


if __name__ == "__main__":
    sol = Solution2()
    # s = "()[]{}"
    s = "(()())"
    res = sol.isValid(s)
    print(res)
