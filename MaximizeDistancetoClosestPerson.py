"""

"""

from itertools import islice
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def maxDisttoClosest(self, seats):
        people = (i for i, s in enumerate(seats) if s)
        prev, future = None, next(people)

        ans = 0
        for i, s in enumerate(seats):
            if s:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float("inf") if not prev else i - prev
                right = float("inf") if not future else future - i
                ans = max(ans, min(left, right))
        return ans


if __name__ == "__main__":
    sol = Solution()
    seats = [1, 0, 0, 0, 1, 0, 1]
    res = sol.maxDisttoClosest(seats)
    print(res)
