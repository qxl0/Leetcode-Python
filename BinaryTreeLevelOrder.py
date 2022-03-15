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

    def levelOrder2(self, root):
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            # level = [kid for n in level for kid in (n.left, n.right) if kid]
            temp = []
            for n in level:
                for kid in [n.left, n.right]:
                    if kid:
                        temp.append(kid)
            level = temp
        return res

    def levelOrder3(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans


if __name__ == "__main__":
    sol = Solution()
    root = createTree([3, 9, 20, None, 13, 15, 7])
    print(sol.levelOrder2(root))
