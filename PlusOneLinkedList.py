# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from helpers.LinkedList import ListNode


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        not9 = dummy
        # first node val != 9 from right direction
        # xxx92xx999
        #       ^
        while head:
            if head.val != 9:
                not9 = head
            head = head.next
        # add 1 to it,
        # move to 9
        not9.val += 1
        not9 = not9.next

        # change to 0 for
        # all 9
        while not9:
            not9.val = 0
            not9 = not9.next
        # could return dummy.next or dummy
        # depends on its val
        return dummy if dummy.val != 0 else dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(9)
    res = sol.plusOne(head)
    print(res)
