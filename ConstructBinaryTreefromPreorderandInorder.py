import helpers.TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        node = helpers.TreeNode.TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        l = inorder[0:pos]
        l_p = preorder[1 : 1 + len(l)]
        r_p = preorder[1 + len(l) :]
        r = inorder[pos + 1 :]
        node.left = self.buildTree(l_p, l)
        node.right = self.buildTree(r_p, r)
        return node


class Solution2:
    def buildTree(self, preorder, inorder):
        root = None
        if inorder:
            loc = inorder.index(preorder.pop(0))
            root = helpers.TreeNode.TreeNode(inorder[loc])
            root.left = self.buildTree(preorder, inorder[:loc])
            root.right = self.buildTree(preorder, inorder[loc + 1 :])
        return root


if __name__ == "__main__":
    sol = Solution2()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = sol.buildTree(preorder, inorder)
    print("ans is", res)
