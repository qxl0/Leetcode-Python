from collections import Counter
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        count = Counter(deck)
        return reduce(gcd, count.values()) > 1


if __name__ == "__main__":
    sol = Solution()
    deck = [1, 1, 2, 2, 2]
    res = sol.hasGroupsSizeX(deck)
    print(res)
