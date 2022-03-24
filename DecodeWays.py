from typing import List

"""
91. Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""


class Solution:
    # O(n) space
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        if s[0] == "0":
            return 0
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    # s = "226"
    s = "12"
    res = sol.numDecodings(s)
    print("result is: ", res)
