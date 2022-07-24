from bisect import bisect_left
from collections import Counter
import heapq
from math import inf
from re import I
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        h = {}
        for i in range(len(names)):
            fn = names[i]
            if fn in h:
                k = h[fn]
                while f"{fn}({k})" in h:
                    k += 1
                h[fn] = k
                tmp = f"{fn}({k})"
                h[tmp] = 1
                fn = tmp
            else:
                h[fn] = 1
            ans.append(fn)
        return ans


if __name__ == "__main__":
    sol = Solution()
    names = ["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]
    res = sol.getFolderNames(names)
    print(res)
