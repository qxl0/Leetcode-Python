"""
1249. Minimum Remove to Make Valid Parentheses
Medium

4638

78

Add to List

Share
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""


from this import d


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "lee(t(c)o)de)"
    res = sol.minRemoveToMakeValid(s)
    print(res)
