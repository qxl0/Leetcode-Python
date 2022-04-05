"""
2116. Check if a Parentheses String Can Be Valid
Medium

445

18

Add to List

Share
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        freeL, freeR, degree = 0, 0, 0
        for c, lock in zip(s, locked):
            if c == "(":
                degree += 1
                if lock == "0":
                    freeL += 1
            else:
                degree -= 1
                if lock == "0":
                    freeR += 1
            if degree < 0:
                if not freeR:
                    return False
                freeR -= 1
                degree += 2
            freeL = min(degree // 2, freeL)
        return degree == freeL * 2


class Solution2:
    def canBeValid(self, s, locked):
        if len(s) % 2 != 0:
            return False
        lower, upper = 0, 0
        for c, lock in zip(s, locked):
            if lock == "1":
                if c == "(":
                    lower += 1
                    upper += 1
                else:
                    lower -= 1
                    upper -= 1
            else:  # *
                upper += 1
                lower -= 1
            if lower < 0:
                lower += 2
            if upper < 0:
                return False
        return lower == 0  # unmatched ( must be 0


if __name__ == "__main__":
    sol = Solution2()
    # s = "))()))"
    # locked = "010100"
    # s = "))"
    # locked = "01"
    s = "())(())((())))(()())())()))))()("
    locked = "11100101100001001111010110101011"
    res = sol.canBeValid(s, locked)
    print(res)
