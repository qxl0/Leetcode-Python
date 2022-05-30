import sys
from typing import List


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ugly = [a]
        ia, ib, ic = 0, 0, 0
        i = 1
        while i < n:
            ua, ub, uc = a * ugly[ia], b * ugly[ib], c * ugly[ic]
            umin = min(ua, ub, uc)
            if umin == ua:
                ia += 1
            if umin == ub:
                ib += 1
            if umin == uc:
                ic += 1
            ugly.append(umin)
            i += 1
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    for line in sys.stdin:
        if "q" == line.rstrip():
            break
        n = int(line.rstrip())
        res = sol.nthUglyNumber(n)
        print("Ans is: ", res)
