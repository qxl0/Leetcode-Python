from collections import Counter, deque
from heapq import heapify, heappush, heappop


from bisect import bisect, bisect_left
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ret = 0
        for w in words:
            if w.find(pref) == 0:
                ret += 1
        return ret


if __name__ == "__main__":
    sol = Solution()
    words = ["pay", "attention", "practice", "attend"]
    pref = "at"
    res = sol.prefixCount(words, pref)
    print("result is: ", res)
