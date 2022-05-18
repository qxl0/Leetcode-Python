import collections

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


if __name__ == "__main__":
    sol = Solution()
    s = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    root = TreeNode.to_binary_tree(s)
    p = 5
    q = 4
    res = sol.lowestCommonAncestor(root, p, q)
    print("Ans is: ", res)
