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
        res = set()
        n = len(text)

        def check(str):
            l = len(str)
            if l % 2 != 0:
                return False
            if str[: l // 2] == str[l // 2 :]:
                return True
            return False

        for i in range(n):
            for j in range(i + 1, n + 1):
                if check(text[i : j + 1]):
                    res.add(text[i : j + 1])
        return len(res)


if __name__ == "__main__":
    sol = Solution()
    text = "abcabcabc"
    res = sol.distinctEchoSubstrings(text)
    print(res)
