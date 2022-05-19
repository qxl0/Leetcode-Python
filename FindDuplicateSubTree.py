import collections
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root):
        def trv(root):
            if not root:
                return "None"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct

        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]


class Solution2:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        key2Id, key2count = {}, {}
        res = []

        def getId(node):
            if not node:
                return -1

            key = (
                str(node.val)
                + "#"
                + str(getId(node.left))
                + "#"
                + str(getId(node.right))
            )
            if key not in key2Id:
                key2Id[key] = len(key2Id)
                key2count[key] = 1
            else:
                key2count[key] += 1
                if key2count[key] == 2:
                    res.append(node)

            return key2Id[key]

        getId(root)
        return res

    def findDuplicateSubtrees2(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        key2count = {}
        res = []

        def getId(node):
            if not node:
                return ""

            key = str(node.val) + "#" + getId(node.left) + "#" + getId(node.right)
            if key not in key2count:
                key2count[key] = 1
            else:
                key2count[key] += 1
                if key2count[key] == 2:
                    res.append(node)

            return key

        getId(root)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    root = TreeNode.to_binary_tree(s)
    p = 5
    q = 4
    res = sol.findDuplicateSubtrees(root)
    print("Ans is: ", res)
