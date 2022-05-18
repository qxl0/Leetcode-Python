from helpers.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, p: "TreeNode", q: "TreeNode") -> "TreeNode":
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1


if __name__ == "__main__":
    sol = Solution()
    # res = sol.lowestCommonAncestor(root, p, q)
    # s = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # root = to_binary_tree(s)
    # p = 5
    # q = 1
    s = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode.to_binary_tree(s)
    res = sol.lowestCommonAncestor(root, p, q)
    print("Ans is: ", res)
