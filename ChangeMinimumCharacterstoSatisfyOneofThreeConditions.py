from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import functools
from math import inf
from typing import List


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ans = inf
        aCount, bCount = Counter(a), Counter(b)
        for th in range(1, 26):
            # print(chr(ord('a')+th))
            change = 0
            for i in range(th, 26):
                # print(chr(ord('a')+i))
                change += aCount[chr(ord("a") + i)]
            for i in range(th):
                change += bCount[chr(ord("a") + i)]
            # print(change)
            ans = min(ans, change)

            change = 0
            for i in range(th, 26):
                change += bCount[chr(ord("a") + i)]
            for i in range(th):
                change += aCount[chr(ord("a") + i)]
            # print(change)
            ans = min(ans, change)

        for th in range(26):
            change = 0
            for i in range(26):
                if i != th:
                    change += aCount[chr(ord("a") + i)]
                    change += bCount[chr(ord("a") + i)]
            ans = min(ans, change)

        return ans


if __name__ == "__main__":
    sol = Solution("a" "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    a = "a"
    b = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    res = sol.minCharacters(a, b)
    print(res)
