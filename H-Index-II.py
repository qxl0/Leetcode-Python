from collections import Counter
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            # print(m,"--", citations[m])
            if citations[m] == n - m:
                return n - m
            elif citations[m] > n - m:
                l = m + 1
            else:
                r = m - 1
        return n - l


if __name__ == "__main__":
    sol = Solution()
    citations = [1, 3, 3, 5, 100]
    res = sol.hIndex(citations)
    print(res)
