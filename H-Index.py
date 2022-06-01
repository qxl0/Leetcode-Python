from collections import Counter
from typing import List


class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        n = len(citations)
        i = 0
        while i < n and citations[i] > i:
            i += 1
        return i


if __name__ == "__main__":
    sol = Solution()
    citations = [1, 3, 3, 5, 100]
    res = sol.hIndex(citations)
    print(res)
