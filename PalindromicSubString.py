class Solution:
    """
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.
    Example 1:

    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
    Example 2:

    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    """

    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            res += self.helper(s, i, i)  # aba
            res += self.helper(s, i, i + 1)
        return res

    def helper(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    res = sol.countSubstrings(s)
    print(res)
