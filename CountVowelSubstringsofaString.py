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
        nonvows = "bcdfghjklmnpqrstvwxyz"
        n = len(word)

        def valid(s):
            ret = all(i in s for i in vows) and not any(i in s for i in nonvows)
            # if ret:
            # print(ret, s)
            return ret

        ret = 0
        for i in range(n):
            for l in range(5, n + 1):
                if i + l > n:
                    continue
                cur = word[i : i + l]
                if valid(cur):
                    # print(i,l, cur)
                    ret += 1
        return ret


class Solution2:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = ("a", "e", "i", "o", "u")

        result = 0
        start = 0
        vowel_idx = {}
        for idx, c in enumerate(word):
            if c in vowels:
                if not vowel_idx:
                    start = idx
                vowel_idx[c] = idx
                if len(vowel_idx) == 5:
                    result += min(vowel_idx.values()) - start + 1
            elif vowel_idx:
                vowel_idx = {}

        return result


if __name__ == "__main__":
    sol = Solution2()
    word = "aeuioauo"
    res = sol.countVowelSubstrings(word)
    print("result is: ", res)
