"""
148. Sort List
Medium

7016

230

Add to List

Share
Given the head of a linked list, return the list after sorting it in ascending order.
"""


from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not head or not head.next:
            return head

        def getMid(head):
            if not head or not head.next:
                return head
            slow, fast = None, head
            while fast and fast.next:
                if not slow:
                    slow = head
                else:
                    slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid

        def merge(left, right):
            pre = dummy = ListNode(0)
            while left or right:
                if left and right:
                    if left.val < right.val:
                        pre.next = left
                        left = left.next
                        pre = pre.next
                    else:
                        pre.next = right
                        right = right.next
                        pre = pre.next
                elif left:
                    pre.next = left
                    left = left.next
                    pre = pre.next
                elif right:
                    pre.next = right
                    right = right.next
                    pre = pre.next
            return dummy.next

        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)


if __name__ == "__main__":
    sol = Solution()
    lst = [4, 2, 3, 1]
    l = LinkedList()
    head = l.lst2link(lst)
    res = sol.sortList(head)
    print("Ans is: ", res)
