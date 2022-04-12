"""
124. Binary Tree Maximum Path Sum
Hard

9118

529

Add to List

Share
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""


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
    max_path = float("-inf")

    def maxPathSum(self, root):
        def get_max_gain(node):
            if not node:
                return 0
            leftSum = max(get_max_gain(node.left), 0)
            rightSum = max(get_max_gain(node.right), 0)

            # calculate the current max_path if current node is root
            curr_max_path = node.val + leftSum + rightSum
            self.max_path = max(self.max_path, curr_max_path)

            # return the max_gain this branch contribute
            return node.val + max(leftSum, rightSum)

        get_max_gain(root)
        return self.max_path


if __name__ == "__main__":
    sol = Solution()
    root = createTree([-10, 9, 20, None, None, 15, 7])
    res = sol.maxPathSum(root)
    print("max Sum of the tree is", res)
