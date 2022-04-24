"""
173. Binary Search Tree Iterator
Medium

5908

394

Add to List

Share
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
"""


from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.l = []
        self.curr = 0
        self.inorder(self.root)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.l.append(node)
        self.inorder(node.right)

    def next(self) -> int:
        ret = None
        if self.curr < len(self.l):
            ret = self.l[self.curr].val
            self.curr += 1
        return ret

    def hasNext(self) -> bool:
        return self.curr < len(self.l)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([7, 3, 15, None, None, 9, 20])
    sol.next()
    sol.next()
    res = sol.hasNext()
    sol.next()

    res = sol.hasNext()
    sol.next()
    res = sol.hasNext()
    sol.next()
    print(res)
