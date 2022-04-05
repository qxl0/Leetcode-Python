"""
22. Generate Parentheses
Medium

12317

480

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n):
        res = []

        def helper(left, right, curr):
            print(f"l={left}, r={right}")
            if len(curr) == 2 * n:
                res.append(curr)
            if 0 < left:
                helper(left - 1, right, curr + "(")
            if right > left and right > 0:
                helper(left, right - 1, curr + ")")

        helper(n, n, "")
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 2
    res = sol.generateParenthesis(n)
    print(res)
