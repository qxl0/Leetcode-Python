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


class Codec:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """


if __name__ == "__main__":
    sol = Codec()
    root = Node.totree(
        [
            1,
            null,
            2,
            3,
            4,
            5,
            null,
            null,
            6,
            7,
            null,
            8,
            null,
            9,
            10,
            null,
            null,
            11,
            null,
            12,
            null,
            13,
            null,
            null,
            14,
        ]
    )
    res = sol.serialize(root)
    res2 = sol.deserialize(res)
    print(res2)
