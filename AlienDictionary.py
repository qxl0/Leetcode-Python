"""
892 · Alien Dictionary
Algorithms
Hard
Accepted Rate
28%

DescriptionSolutionNotesDiscussLeaderboard
Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of 
non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
You must write an algorithm that runs in O(n) time.
"""
import collections
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def alien_order(self, words):
        def build_graph(words):
            graph = collections.defaultdict(list)
            n = len(words)
            for i in range(n - 1):
                w1, w2 = words[i], words[i + 1]
                minlen = min(len(w1), len(w2))
                for j in range(minlen):
                    if w1[j] != w2[j]:
                        graph[w1[j]].append(w2[j])
                        break
                    if j == minlen - 1:
                        return None
            return graph

        def topological_order(graph):
            indegree = {node: 0 for node in graph}
            for node in graph:
                for neigh in graph[node]:
                    if neigh not in indegree:
                        indegree[neigh] = 0
                    indegree[neigh] += 1
            queue = [node for node in graph if indegree[node] == 0]
            heapify(queue)
            top_order = ""
            while queue:
                node = heappop(queue)
                top_order += node
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        heappush(queue, neigh)
            if len(top_order) == len(graph):
                return top_order
            return ""

        graph = build_graph(words)
        if not graph:
            return ""
        return topological_order(graph)


if __name__ == "__main__":
    sol = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    res = sol.alien_order(words)
    print("result is: ", res)
