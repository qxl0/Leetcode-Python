"""
394. Decode String
Medium

8025

343

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
"""


from math import floor
from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "2[a]2[bc]"
    res = sol.decodeString(s)

    print(res)
