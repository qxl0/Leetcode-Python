"""
536. Construct Binary Tree from String
Medium

911

148

Add to List

Share
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.
"""


from math import floor
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if len(s) == 0:
            return None

        def helper(cur):
            negative = False
            if s[cur] == "-":
                negative = True
                cur += 1
            number = 0
            while cur < len(s) and s[cur].isdigit():
                number = number * 10 + int(s[cur])
                cur += 1

            number = -number if negative else number

            node = TreeNode(number)

            if cur < len(s) and s[cur] == "(":
                node.left, cur = helper(cur + 1)
            if node.left and cur < len(s) and s[cur] == "(":
                node.right, cur = helper(cur + 1)

            return node, cur + 1 if cur < len(s) and s[cur] == ")" else cur

        return helper(0)[0]


if __name__ == "__main__":
    sol = Solution()
    s = "4(2(3)(1))(6(5))"
    res = sol.str2tree(s)

    print(res)
