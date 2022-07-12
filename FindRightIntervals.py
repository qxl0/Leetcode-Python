"""

"""

import heapq
from itertools import islice
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts, ends = [], []
        for i, (start, end) in enumerate(intervals):
            starts.append((start, i))
            ends.append((end, i))
        heapq.heapify(starts)
        heapq.heapify(ends)
        output = [-1] * len(intervals)
        while ends:
            end, i = heapq.heappop(ends)
            # find the smallest start >= end in the sytem
            while starts and starts[0][0] < end:
                starts.pop(0)
            if not starts:
                break
            # starts[0][0]>=end
            output[i] = starts[0][1]
        return output


if __name__ == "__main__":
    sol = Solution()
    intervals = [(1, 2), (2, 3), (0, 1), (3, 4)]
    res = sol.findRightInterval(intervals)
    print(res)
