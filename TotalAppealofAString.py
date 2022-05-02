"""
2262. Total Appeal of A String
Hard

198

6

Add to List

Share
The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.
"""
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def appealSum(self, s: str) -> int:
        # xxxaxxxb... s[i] = a and s[j] = b, s[i] is last char a before b
        # we want to count how many substring ending at s[j] contains char a
        # xxxaxxxb, xxaxxxb, xaxxxb, axxxb, i+1
        # so res += i+1
        # we repeatly do this for every s[i] and every one of 26 characters
        res = 0
        last = {}
        for i, c in enumerate(s):
            last[c] = i + 1
            res += sum(last.values())
        return res


class Solution2:
    def appealSum(self, s):
        n = len(s)
        dp = [-1] * (n + 1)
        lastIdx = [-1] * 26
        ans = 0
        for i, ch in enumerate(s):
            c = ord(ch) - ord("a")
            dp[i + 1] = dp[i] + i - lastIdx[c]
            ans += dp[i + 1]

            lastIdx[c] = i
        print(dp)
        return ans


class Solution3:
    def appealSum(self, s):
        res, n = 0, len(s)
        last = {ch: -1 for ch in ascii_lowercase}
        for i, ch in enumerate(s):
            res += (i - last[ch]) * (n - i)
            last[ch] = i
        return res


if __name__ == "__main__":
    sol = Solution3()
    # s = "abbca"
    s = "abb"
    res = sol.appealSum(s)
    print(res)
