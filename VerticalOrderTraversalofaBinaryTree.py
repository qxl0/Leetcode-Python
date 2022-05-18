from typing import Collection, List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = Collection.defaultdict(list)

        def helper(node, r, c):
            if not node:
                return
            ans[c].append(node.val)
            helper(node.left, r + 1, c - 1)
            helper(node.left, r + 1, c + 1)

        helper(root, 0, 0)
        return dict(sorted(ans.items())).values()


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([3, 9, 20, None, None, 15, 7])
    res = sol.verticalTraversal(root)

    print(res)
