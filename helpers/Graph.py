class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True

    def number_of_neighbors(self):
        return len(self.neighbors)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, value, neighbors=None):
        self.nodes.append(Node(value, neighbors))

    def find_node(self, value):
        for node in self.nodes:
            if node.val == value:
                return node
        return None

    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 and node2:
            node1.add_neighbor((node2, weight))
            node2.add_neighbor((node1, weight))
        else:
            print("Error: One or more nodes were not found")

    def number_of_nodes(self):
        return f"The Graph has {len(self.nodes)} nodes"

    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighbors in node_one.neighbors:
            if neighbors[0].val == node_two.val:
                return True
        return False
