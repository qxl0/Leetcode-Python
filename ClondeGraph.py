"""
133. Clone Graph
Medium

5591

2477

Add to List

Share
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List

from helpers.Graph import Node


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        m = {}

        def helper(node):
            if not node:
                return None
            if node in m:
                return m[node]
            m[node] = Node(node.val)

            for neigh in node.neighbors:
                m[node].neighbors.append(helper(neigh))

            return m[node]

        return helper(node)


if __name__ == "__main__":
    sol = Solution()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    res = sol.cloneGraph(adjList)
    print(res)
