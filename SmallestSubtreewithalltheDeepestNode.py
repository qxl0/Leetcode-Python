import collections
from SerializeDeserializebinaryTree import BinaryTreeSerializer

from helpers.TreeNode import TreeNode
from helpers.BinaryTreeSerializer import BinaryTreeSerializer


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))

        def dfs(node):
            # Return the result of the subtree at this node.
            if not node:
                return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist:
                return Result(L.node, L.dist + 1)
            if L.dist < R.dist:
                return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node


if __name__ == "__main__":
    sol = Solution()
    # str = "13Nn25Nl36Nl42Nr57Nl64Nr71Nr80Nl98Nr"
    root = TreeNode.to_binary_tree(
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None]
    )
    res = sol.subtreeWithAllDeepest(root)
    print("Ans is: ", res)
