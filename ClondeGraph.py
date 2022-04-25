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

class Node:
  def __init__(self, val=0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pass


if __name__ == "__main__":
    sol = Solution()
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    res = sol.cloneGraph(adjList)
    print(res)
