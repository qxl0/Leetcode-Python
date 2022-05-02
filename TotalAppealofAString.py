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
from string import ascii_uppercase


class Solution:
    def appealSum(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "abbca"
    res = sol.appealSum(s)
    print(res)
