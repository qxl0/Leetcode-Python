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
        output = []

        def helper(node, output):
            if not node:
                output.append("#")
                return
            output.append(str(node.val))
            helper(node.left, output)
            helper(node.right, output)

        helper(root, output)
        return ",".join(output)

    def deserialize(self, data):
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "#":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        node = dfs()
        return node


class Solution2:
    def serialize(self, root):
        serializedlist = []
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def helper(node, idx, parentId, lorR="n"):
            if not node:
                return
            serializedlist.append(chr(idx[0] + 48))
            val = node.val
            serializedlist.append(chr(val + 48))
            serializedlist.append(chr(parentId + 48) if parentId != -1 else "N")
            serializedlist.append(lorR)

            parentid = idx[0]
            if node.left:
                idx[0] += 1
                helper(node.left, idx, parentId, "l")
            if node.right:
                idx[0] += 1
                helper(node.right, idx, parentId, "r")

        if not root:
            return ""
        Index = [1]
        helper(root, Index, -1)
        return "".join(serializedlist)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(data):
            nodesMap = {}
            for i in range(0, len(data), 4):
                id = ord(data[i]) - 48
                val = ord(data[i + 1]) - 48
                parentId = ord(data[i + 2]) - 48
                nodesMap[id] = (parentId, TreeNode(val))

            for i in range(4, len(data), 4):
                id = ord(data[i]) - 48
                parentId = ord(data[i + 2]) - 48
                node = nodesMap[id][1]
                parent = nodesMap[parentId][1]
                leftOrRight = data[i + 3]
                # add left,right
                if leftOrRight == "l":
                    parent.left = node
                elif leftOrRight == "r":
                    parent.right = node

        if not data:
            return None
        return helper(data)


class Solution3:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append("#")

        vals = []
        doit(root)
        return " ".join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    sol = Solution2()
    s = [1, 2, 3, None, None, 4, 5]
    # root = TreeNode.to_binary_tree(s)
    # res = sol.serialize(root)
    res = "11Nn221l331r443l553r"
    print("ans is ", res)
    node = sol.deserialize(res)
