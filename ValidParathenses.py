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


class Solution3:
    def isValid(self, s: str) -> bool:
        opened = ["[", "{", "("]
        closed = ["]", "}", ")"]
        stack = []
        for c in s:
            if c in opened:
                stack.append(c)
            else:
                if len(stack) != 0 and stack[-1] == opened[closed.index(c)]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    # s = "()[]{}"
    s = "(()())"
    # s = "()"
    res = sol.isValid(s)
    print(res)
