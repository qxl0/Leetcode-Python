from calendar import c
from collections import defaultdict
import heapq
from typing import List


class TrieNode:
    def __init__(self):
        self.children, self.is_word = {}, False

    @staticmethod
    def construct_trie(words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                node.children.setdefault(c, TrieNode())
                node = node.children[c]
            node.is_word = True
        return root


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        adj = defaultdict(list)
        for i, d in enumerate(distance):
            adj[i].append((d, i + 1))
        vis = set()
        q = [(0, start)]
        vis.add(start)
        dist = 0
        while q:
            d, cur = heapq.heappop(q)

            if cur == destination:
                return dist

            # add neig to q
            for d, nei in adj[cur]:
                if nei not in vis:
                    vis.add(nei)
                    heapq.heappush(q, (d, nei))


if __name__ == "__main__":
    sol = Solution()
    calories = [1, 2, 3, 4, 5]
    res = sol.dietPlanPerformance(calories, k, 3, 3)
    print(res)
