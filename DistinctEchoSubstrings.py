"""
1316. Distinct Echo Substrings
Hard

182

172

Add to List

Share
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    text = "abcabcabc"
    res = sol.distinctEchoSubstrings(text)
    print(res)
