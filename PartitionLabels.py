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
import heapq
import sys
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pass


if __name__ == "__main__":
    s = Solution()
    str = "ababcbacadefegdehijhklij"
    res = s.partitionLabels(str)
    print("Ans is : ", res)
