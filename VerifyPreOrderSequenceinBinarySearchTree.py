"""
## (**255) Verify Preorder Sequence in Binary Search Tree**

**Medium**

927

70

Add to List

Share

Given an array of **unique** integers `preorder`, return `true` *if it is the correct preorder traversal sequence of a binary search tree*.
"""


from math import floor
from typing import List


class Solution:
    def verifyPreorder(self, preorder):
        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True


class Solution2:
    def verifyPreorder(self, preorder):
        # stack = preorder[:i], reuse preorder as stack
        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
        return True


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 1, 3, 6]
    res = sol.verifyPreorder(nums)

    print(res)
