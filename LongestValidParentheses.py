"""
2. Longest Valid Parentheses
Hard

7467

254

Add to List

Share
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""


from this import d


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = ")()())"
    s = "(()"
    res = sol.longestValidParentheses(s)
    print(res)
