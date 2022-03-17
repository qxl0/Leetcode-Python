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
