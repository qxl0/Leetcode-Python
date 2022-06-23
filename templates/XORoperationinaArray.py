"""
"""


from typing import List


class Solution:
    def xorOperation(self, n, start):
        def helperB(n, start):
            if n % 2 == 0:
                return (n // 2) & 1
            return ((n // 2) & 1) ^ (start + n - 1)

        def helperA(n, start):
            if start & 1:
                return (start - 1) ^ helperB(n + 1, start - 1)
            return helperB(n, start)

        ret = 2 * helperA(n, start // 2)
        if n & start & 1:
            ret += 1
        return ret


if __name__ == "__main__":
    sol = Solution()
    n = 2
    start = 8
    for i in range(2, 100, 2):
        res = sol.xorOperation(i, start)
        print(i, start, res)
