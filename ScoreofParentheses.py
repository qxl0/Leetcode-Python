from collections import Counter
import heapq
from math import inf
from typing import List


class Solution(object):
    def scoreOfParentheses(self, S):
        def F(i, j):
            # Score of balanced string S[i:j]
            ans = bal = 0

            # Split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == "(" else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i + 1, k)
                    i = k + 1

            return ans

        return F(0, len(S))


if __name__ == "__main__":
    sol = Solution()
    S = "(()())"
    res = sol.scoreOfParentheses(S)
    print(res)
