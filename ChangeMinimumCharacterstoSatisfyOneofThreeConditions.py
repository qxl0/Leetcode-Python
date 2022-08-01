from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import functools
from math import inf
from typing import List


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ans = inf
        aCount, bCount = Counter(a), Counter(b)
        for i in "abcdefghijklmnopqrstuvwxyz":
            # check a
            op1 = 0
            for ch, cnt in aCount.items():
                if ch != i:
                    op1 += cnt
            for ch, cnt in bCount.items():
                if ch != i:
                    op1 += cnt
            ans = min(ans, op1)

            op3 = 0  # all ch in a < b
            for ch, cnt in aCount.items():
                if ch >= i:
                    op3 += cnt
            for ch, cnt in bCount.items():
                if ch < i:
                    op3 += cnt
            ans = min(ans, op3)

            op2 = 0  # all ch in b < a
            for ch, cnt in bCount.items():
                if ch >= i:
                    op2 += cnt
            for ch, cnt in aCount.items():
                if ch < i:
                    op2 += cnt
            ans = min(ans, op2)

        return ans


if __name__ == "__main__":
    sol = Solution()
    a = "a"
    b = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    res = sol.minCharacters(a, b)
    print(res)
