"""
763. Partition Labels
Medium

7539

287

Add to List

Share
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""
import collections
import enum
import heapq
import sys
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result, lastSeen, maxLastSeen, count = [], {}, 0, 0
        for i, char in enumerate(s):
            lastSeen[char] = i
        for i, char in enumerate(s):
            maxLastSeen = max(maxLastSeen, lastSeen[char])
            count += 1
            if i == maxLastSeen:
                result.append(count)
                count = 0
        return result


class Solution2:
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}

        start = end = 0
        output = []

        for i, c in enumerate(s):
            end = max(end, last[c])

            if i == end:
                output.append(end - start + 1)
                start = i + 1
        return output


if __name__ == "__main__":
    s = Solution2()
    str = "ababcbacadefegdehijhklij"
    res = s.partitionLabels(str)
    print("Ans is : ", res)
