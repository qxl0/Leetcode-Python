"""
332. Reconstruct Itinerary
Hard

3767

1545

Add to List

Share
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
 
"""


import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += (b,)
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            adj[a] += (b,)
        route = []

        def visit(c):
            while adj[c]:
                visit(adj[c].pop())
            route.append(c)

        visit("JFK")
        return route[::-1]


if __name__ == "__main__":
    s = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = s.findItinerary2(tickets)
    print("Ans is:", res)
