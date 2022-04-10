"""
2. Add Two Numbers
Medium

17696

3669

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        pass


if __name__ == "__main__":
    s = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    res = s.copyRandomList(l1, l2)
    print(res)
