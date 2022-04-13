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

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first, second = l1, l2
        nextval = 0
        dummy = curr = ListNode(-1)
        while first and second:
            val1, val2 = int(first.val), int(second.val)
            curr.next = ListNode((val1 + val2 + nextval) % 10)
            nextval = (val1 + val2 + nextval) // 10
            first = first.next
            second = second.next
            curr = curr.next
        while first:
            val1 = int(first.val)
            curr.next = ListNode((val1 + nextval) % 10)
            nextval = (val1 + nextval) // 10
            first = first.next
            curr = curr.next
        while second:
            val2 = int(second.val)
            curr.next = ListNode((val2 + nextval) % 10)
            nextval = (val2 + nextval) // 10
            second = second.next
            curr = curr.next
        if nextval:
            curr.next = ListNode(nextval)

        return dummy.next


class Solution2:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = curr = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


if __name__ == "__main__":
    s = Solution2()
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = s.addTwoNumbers(l1, l2)
    print("Ans is: ", res)
