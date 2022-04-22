"""
455. Assign Cookies
Easy

1410

157

Add to List

Share
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""
import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ret = 0
        g.sort()
        s.sort()
        visited = set()
        for cookie in s:
            for i, kid in enumerate(g):
                if i in visited:
                    continue
                if cookie >= kid:
                    ret += 1
                    visited.add(i)
                    break

        return ret


class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie, kid = 0, 0
        while kid < len(g) and cookie < len(s):
            if s[cookie] >= g[kid]:
                kid += 1
            cookie += 1
        return kid


if __name__ == "__main__":
    sol = Solution()
    g = [1, 2, 3]
    s = [3]
    res = sol.findContentChildren(g, s)
    print("Ans is ", res)
