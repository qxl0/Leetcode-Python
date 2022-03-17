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
    def buildTree(prorder, inorder):
        pass


if __name__ == "__main__":
    sol = Solution()
    root = createTree([-10, 9, 20, None, None, 15, 7])
    res = sol.maxPathSum(root)
    print("max Sum of the tree is", res)
