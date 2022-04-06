"""
678. Valid Parenthesis String
Medium

3295

81

Add to List

Share
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        lower, upper = 0, 0  # min # of (, max # of (
        for c in s:
            if c == "*":
                lower -= 1
                upper += 1
            elif c == "(":
                lower += 1
                upper += 1
            else:  # )
                lower -= 1
                upper -= 1
            if lower < 0:
                lower += 1
            if upper < 0:
                return False
        return lower == 0


if __name__ == "__main__":
    sol = Solution()
    s = "(*))"
    # s = "(*)"
    # s = "(*)("
    res = sol.checkValidString(s)
    print(res)
