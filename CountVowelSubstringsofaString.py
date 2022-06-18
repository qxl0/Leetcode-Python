"""

"""
import collections
import heapq
import sys
from typing import (
    List,
)


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vows = ["a", "e", "i", "o", "u"]
        nonvows = "bcdfghjpqrstvwxyz"
        n = len(word)

        def valid(s):
            ret = all(i in s for i in vows) and not any(i in s for i in nonvows)
            # if ret:
            # print(ret, s)
            return ret

        ret = 0
        for i in range(n):
            for l in range(5, n + 1 - 5):
                cur = word[i : i + l]
                if valid(cur):
                    print(i, i + l, cur)
                    ret += 1
        return ret


if __name__ == "__main__":
    sol = Solution()
    word = "aeuioauo"
    res = sol.countVowelSubstrings(word)
    print("result is: ", res)
