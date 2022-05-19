import collections
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""

        def getId(node):
            return getId(node.left) + getId(node.right) + [node.val] if node else []

        return " ".join(map(str, getId(root)))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""

        def helper(lower=float("-inf"), upper=float("inf")):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(" ") if x]
        return helper()


if __name__ == "__main__":
    sol = Codec()
    root = TreeNode.to_binary_tree([2, 1, 3])
    res = sol.serialize(root)
    print("Ans is: ", res)
    node = sol.deserialize(res)
