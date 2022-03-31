"""
5. Longest Palindromic Substring
Medium

16820

984

Add to List

Share
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def findPalindromeFrom(s, l, r):
            while l > 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(len(s)):
            tmp = findPalindromeFrom(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = findPalindromeFrom(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res


if __name__ == "__main__":
    sol = Solution()
    # s = "babad"
    s = "cbbd"
    res = sol.longestPalindrome(s)
    print(res)
