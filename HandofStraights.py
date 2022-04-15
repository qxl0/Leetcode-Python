"""
846. Hand of Straights
Medium

1319

112

Add to List

Share
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""
import collections
import heapq
import sys
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = collections.Counter(hand)
        for y in sorted(count):
            while count[y] > 0:
                for k in range(y, y + groupSize):
                    count[k] -= 1
                    if count[k] < 0:
                        return False
        return True

    def isNStraightHand2(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = {}
        for h in hand:
            count[h] = count.get(h, 0) + 1

        minq = list(count.keys())
        heapq.heapify(minq)
        while minq:
            first = minq[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    heapq.heappop(minq)
        return True


if __name__ == "__main__":
    s = Solution()
    hand = [8, 1, 2, 3, 6, 2, 3, 4, 7]
    groupSize = 3
    res = s.isNStraightHand2(hand, groupSize)
    print("Ans is : ", res)
