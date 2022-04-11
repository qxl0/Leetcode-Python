class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(lst):
    return helper(lst, 0)


def helper(lst, i):
    if i >= len(lst) or not lst[i]:
        return None
    curr = TreeNode(lst[i]) if lst[i] else None
    curr.left = helper(lst, 2 * i + 1)
    curr.right = helper(lst, 2 * i + 2)

    return curr


class Solution:
    def isSubtree(self, root, subRoot):
        def isSametree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None and node2 or node1 and node2 is None:
                return False
            return (
                node1.val == node2.val
                and isSametree(node1.left, node2.left)
                and isSametree(node1.right, node2.right)
            )

        if not root:
            return False

        return (
            isSametree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.right = TreeNode(1)
    root.right.right.right.left = TreeNode(2)

    subtree = TreeNode(1)
    subtree.right = TreeNode(1)
    subtree.right.left = TreeNode(2)
    res = sol.isSubtree(root, subtree)
    print("Ans is: ", res)
