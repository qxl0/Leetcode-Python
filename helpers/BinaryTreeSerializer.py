from helpers.TreeNode import TreeNode


class BinaryTreeSerializer:
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
        "11Nn221l331r443l553r"
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
