"""
828. Count Unique Characters of All Substrings of a Given String
Hard

1318

178

Add to List

Share
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
"""
from string import ascii_uppercase


class Solution:
    def uniqueLetterString(self, S):
        index = {c: [-1, -1] for c in ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()
    s = "ABAB"
    res = sol.uniqueLetterString(s)
    print(res)
