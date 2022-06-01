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
        print(graph)
        if not graph:
            return ""
        return topological_order(graph)


from collections import defaultdict, Counter, deque


class Solution2:
    def alien_order(self, words: List[str]) -> str:
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
                else:  # Check that second word isn't a prefix of first word.
                    if len(second_word) < len(first_word):
                        return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


class Solution3:
    def alien_order(self, words: List[str]) -> str:
        n = len(words)

        def build_graph(words):
            n = len(words)
            adj = defaultdict(list)
            for i in range(n - 1):
                w1, w2 = words[i], words[i + 1]
                m, n = len(w1), len(w2)
                for i in range(min(n, m)):
                    if w1[i] != w2[i]:
                        adj[w1[i]].append(w2[i])
                        break
            return adj

        adj = build_graph(words)
        indegree = Counter({c: 0 for w in words for c in w})
        # print(indegree)

        for node in adj:
            for nei in adj[node]:
                indegree[nei] += 1
        # print(indegree)
        output = []
        q = deque([c for c in indegree if indegree[c] == 0])
        while q:
            c = q.popleft()
            output.append(c)
            for d in adj[c]:
                indegree[d] -= 1
                if not indegree[d]:
                    q.append(d)
        if len(output) < len(indegree):
            return ""
        else:
            return "".join(output)


if __name__ == "__main__":
    sol = Solution3()
    # words = ["wrt", "wrf", "er", "ett", "rftt"]
    # words = ["ac", "ab", "zc", "zb"]
    words = ["aa", "a"]
    res = sol.alien_order(words)
    print("result is: ", res)
