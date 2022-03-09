from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

def printList(node):
  temp = []
  while node:
    temp.append(node.val)
    node = node.next
  print(temp)

class Solution:
  def reorderList(self, head: Optional[ListNode]):
    slow, fast = head, head
    while fast and fast.next:
      slow, fast = slow.next, fast.next.next

    printList(slow)
    prev, current = None, slow.next
    slow.next = None
    while current:
      temp = current
      current = current.next
      temp.next = prev
      prev = temp

    printList(head)
    printList(prev) 

    dummy = curr = ListNode(0)
    head1, head2 = head, prev
    while head1 and head2:
      if head1:
        curr.next, head1 = head1, head1.next
        curr = curr.next

      if head2:
        curr.next, head2 = head2, head2.next
        curr = curr.next
    curr.next = head1 or head2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
r1 = Solution()

r1.reorderList(head)
