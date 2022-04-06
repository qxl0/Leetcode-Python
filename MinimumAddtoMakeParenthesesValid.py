"""
921. Minimum Add to Make Parentheses Valid
Medium

2401

139

Add to List

Share
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""


from this import d


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        st = []
        for c in s:
            if c == "(":
                st.append(c)
            else:
                if not st:
                    count += 1
                else:
                    st.pop()
        while st:
            st.pop()
            count += 1
        return count


class Solution2:
    def minAddToMakeValid(self, s):
        left, count = 0, 0
        for c in s:
            if c == "(":
                left += 1
            else:
                left -= 1
            if left < 0:
                left = 0
                count += 1
        return left + count


if __name__ == "__main__":
    sol = Solution()
    s = "()))"
    res = sol.minAddToMakeValid(s)
    print(res)
