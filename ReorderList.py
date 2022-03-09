class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def printList(node):
  temp = []
  while node:
    temp.append(node.val)
    node = node.next
  print(temp)

def reorderList(head):
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. find mid
        slow,fast = head, head
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        
        printList(slow.next)
        # 2. reverse second list
        prev, curr = None, slow.next
        slow.next = None # set it to None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        printList(head)
        printList(prev)
        # prev is the head of reversed
        # list
        # 3. merge (head, prev)
        dummy = curr = ListNode(0)
        head1,head2 = head, prev
        while head1 and head2:
            if head1:
                curr.next, head1 = head1,head1.next
                curr = curr.next
            if head2:
                curr.next, head2 = head2, head2.next
                curr = curr.next
        curr.next = head1 or head2

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

printList(head)
reorderList(head)
printList(head)