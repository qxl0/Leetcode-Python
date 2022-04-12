"""
297. Serialize and Deserialize Binary Tree
Hard

6399

250

Add to List

Share
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
"""

from helpers.TreeNode import TreeNode


class Solution:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        pass

    def deserialize(self, data):
        pass


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    sol = Solution()
    s = [1, 2, 3, None, None, 4, 5]
    root = TreeNode.to_binary_tree([-10, 9, 20, None, None, 15, 7])
    res = sol.serialize(root)
    print("ans is ", res)
