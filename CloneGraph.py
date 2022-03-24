"""
133. Clone Graph
Medium

5414

2417

Add to List

Share
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""


import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def addNeighbor(self, n):
        self.neighbors.append(n)


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        visited, m = set(), dict()

        def dfs(node, visited, m):
            if node in visited:
                return
            visited.add(node)
            if node not in m:
                m[node] = Node(node.val)
            for neigh in node.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[node].neighbors.append(m[neigh])
                dfs(neigh, visited, m)

        dfs(node, visited, m)
        return m[node]

    # dfs iteratively
    def cloneGraph2(self, node):
        if not node:
            return node
        m, visited, stack = dict(), set(), collections.deque([node])
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(node)
            if n not in m:
                m[n] = Node(n.val)

            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(neigh)
                stack.append(neigh)
        return m[node]

    # bfs
    def cloneGraph3(self, node):
        if not node:
            return node
        m, visited, queue = {}, set(), collections.deque([node])
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                queue.append(neigh)
        return m[node]


def createNode(adjList):
    #
    if not adjList:
        return None
    if len(adjList) == 1 and len(adjList[0]) == 0:
        return Node(
            1
        )  # For simplicity, each node's value is the same as the node's index (1-indexed)
    nodeMap = collections.defaultdict()
    for i, v in enumerate(adjList):
        if i + 1 not in nodeMap:
            nodeMap[i + 1] = Node(i + 1)
        node = nodeMap[i + 1]
        for e in v:
            if e not in nodeMap:
                nodeMap[e] = Node(e)
            neighbor = nodeMap[e]
            node.addNeighbor(neighbor)
    return nodeMap[1]


if __name__ == "__main__":
    sol = Solution()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = createNode(adjList)
    res = sol.cloneGraph(node)
    print("result is: ", res)
