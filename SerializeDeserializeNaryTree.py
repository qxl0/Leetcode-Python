"""
474. Ones and Zeroes
Medium

2874

324

Add to List

Share
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        if not self.children:
            self.children = []

    def __repr__(self):
        return f"val:{self.val}"

    def add_child(self, obj):
        self.children.append(obj)


class WrappableInt:
    def __init__(self, x):
        self.value = x

    def getValue(self):
        return self.value

    def increment(self):
        self.value += 1


class Codec:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList, WrappableInt(1), None)
        return "".join(serializedList)

    def _serializeHelper(self, root, serializedList, identity, parentId):
        if not root:
            return

        # Own identity
        serializedList.append(chr(identity.getValue() + 48))

        # Actual value
        serializedList.append(chr(root.val + 48))

        # Parent's identity
        serializedList.append(chr(parentId + 48) if parentId else "N")

        parentId = identity.getValue()
        for child in root.children:
            identity.increment()
            self._serializeHelper(child, serializedList, identity, parentId)

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        if not data:
            return None

        return self._deserializeHelper(data)

    def _deserializeHelper(self, data):

        nodesAndParents = {}
        for i in range(0, len(data), 3):
            identity = ord(data[i]) - 48
            orgValue = ord(data[i + 1]) - 48
            parentId = ord(data[i + 2]) - 48
            nodesAndParents[identity] = (parentId, Node(orgValue, []))

        for i in range(3, len(data), 3):

            # Current node
            identity = ord(data[i]) - 48
            node = nodesAndParents[identity][1]

            # Parent node
            parentId = ord(data[i + 2]) - 48
            parentNode = nodesAndParents[parentId][1]

            # Attach!
            parentNode.children.append(node)

        return nodesAndParents[ord(data[0]) - 48][1]


if __name__ == "__main__":
    sol = Codec()
    # root = Node(1)
    # root.add_child(Node(2))

    # node11 = Node(11)
    # node11.add_child(Node(14))
    # node7 = Node(7)
    # node7.add_child(node11)
    # node3 = Node(3)
    # node3.add_child(Node(6))
    # node3.add_child(node7)
    # root.add_child(node3)

    # node8 = Node(8)
    # node8.add_child(Node(12))
    # node4 = Node(4)
    # node4.add_child(node8)
    # root.add_child(node4)

    # node9 = Node(9)
    # node9.add_child(Node(13))
    # node5 = Node(5)
    # node5.add_child(node9)
    # node5.add_child(Node(10))
    # root.add_child(node5)

    # res = sol.serialize(root)
    # 11N2213314635736;57>6841988:<9;51<9;==<>:;
    # 11N2213314635736;57>6841988:<9;51<9;==<>:;
    # print(res)
    res = "11N2213314635736;57>6841988:<9;51<9;==<>:;"
    res2 = sol.deserialize(res)
    print(res2)
