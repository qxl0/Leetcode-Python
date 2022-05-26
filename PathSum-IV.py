"""

"""

import collections
from math import floor
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution(object):
    def pathSum(self, nums):
        self.ans = 0
        root = TreeNode(nums[0] % 10)

        for x in nums[1:]:
            # depth, pos, val = x // 100, x // 10 % 10, x % 10
            depth, pos, val = map(int, str(x))
            pos -= 1
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2**d:
                    # cur.left = cur = cur.left or TreeNode(val)
                    if not cur.left:
                        cur.left = TreeNode(val)
                    cur = cur.left
                else:
                    # cur.right = cur = cur.right or TreeNode(val)
                    if not cur.right:
                        cur.right = TreeNode(val)
                    cur = cur.right
                pos %= 2**d

        def dfs(node, running_sum=0):
            if not node:
                return
            running_sum += node.val
            if not node.left and not node.right:
                self.ans += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)

        dfs(root)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    nums = [113, 215, 221, 314, 336, 425, 478]
    res = sol.pathSum(nums)
    print("Ans is: ", res)
