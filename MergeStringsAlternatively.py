from collections import Counter, deque
from heapq import heapify, heappush, heappop


from bisect import bisect, bisect_left
from itertools import zip_longest
from typing import List


class Solution:
    def mergeAlternately(self, w1, w2):
        return "".join(a + b for a, b in zip_longest(w1, w2, fillvalue=""))


if __name__ == "__main__":
    sol = Solution()
    word1 = "abc"
    word2 = "efghi"
    res = sol.mergeAlternately(word1, word2)
    print("result is: ", res)
