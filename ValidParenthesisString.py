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
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "(*))"
    res = sol.checkValidString(s)
    print(res)
