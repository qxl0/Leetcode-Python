class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd
            tmp = self.findPalindromeFrom(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.findPalindromeFrom(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def findPalindromeFrom(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]


if __name__ == "__main__":
    sol = Solution()
    s = "a"
    res = sol.longestPalindrome(s)
    print(res)
