"""
72. Edit Distance
Hard

8173

92

Add to List

Share
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
"""


import collections
import sys
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    sol = Solution()
    res = sol.minDistance(word1, word2)
    print("Ans is:", res)
