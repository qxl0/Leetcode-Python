import enum
from pytest import LogCaptureFixture


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        res = []
        while q:
            res.append([node.val for node in q])
            temp = []
            for node in q:
                temp.extend([node.left, node.right])
            q = [leaf for leaf in temp if leaf]
        return res


def createTree(lst):
    return helper(lst, 0)


def helper(lst, i):
    if i >= len(lst) or not lst[i]:
        return None
    curr = TreeNode(lst[i]) if lst[i] else None
    curr.left = helper(lst, 2 * i + 1)
    curr.right = helper(lst, 2 * i + 2)

    return curr


if __name__ == "__main__":
    sol = Solution()
    root = createTree([3, 9, 20, None, 13, 15, 7])
    sol.levelOrder(root)
