"""
1541. Minimum Insertions to Balance a Parentheses String
Medium

619

132

Add to List

Share
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.
"""


from this import d


class Solution:
    # two steps process: if singl right, increase count by 1 do whatever required
    #                    if left < 0, increase count by 1 for adding a left
    def minInsertion(self, s: str) -> str:
        left = 0
        count = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                left += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    left -= 1
                    i += 1
                else:  # )(
                    count += 1  # add 1 )
                    left -= 1
            if left < 0:
                count += 1
                left = 0
            i += 1
        return count + left * 2


if __name__ == "__main__":
    sol = Solution()
    # s = "))())("
    # s = "(()))"
    # s = ")))))))"
    # s = "()())))()"
    # s = ")("
    # s = "())("
    # s = "(()))"
    # s = "()())))()"
    s = ")"
    res = sol.minInsertion(s)
    print(res)
