from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import functools
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(queries)

        A = [i for i in range(len(s)) if s[i] == "|"]
        print(A)
        ans = []

        for l, r in queries:
            i = bisect_left(A, l)  # barlst[:i] <l
            j = bisect_right(A, r) - 1  # barlst[j:] >
            # print(i,A[i],j,A[j])
            # between A[i] A[j], total len = A[j]-A[i]-1 excluding two external |
            # inside, there are (j-i-1) |
            # so * count is : A[j]-A[i]-1 - (j-i-1)
            ans.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    res = sol.platesBetweenCandles(s, queries)
    print(res)
