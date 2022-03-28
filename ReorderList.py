"""
143. Reorder List
Medium

5553

204

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


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


def createList(l):
    dummy = curr = ListNode(0)
    for i, v in enumerate(l):
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    # 1. find mid
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    printList(slow.next)
    # 2. reverse second list
    prev, curr = None, slow.next
    slow.next = None  # set it to None
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
    head1, head2 = head, prev
    while head1 and head2:
        if head1:
            curr.next, head1 = head1, head1.next
            curr = curr.next
        if head2:
            curr.next, head2 = head2, head2.next
            curr = curr.next
    curr.next = head1 or head2


# head = createList([1, 2, 3, 4, 5, 6, 7, 8])
head = createList([1, 2, 3])
printList(head)

reorderList(head)
printList(head)
