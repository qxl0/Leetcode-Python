"""
138. Copy List with Random Pointer
Medium

8274

963

Add to List

Share
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


from typing import Optional
from helpers.LinkedList import ListNode
from helpers.LinkedList import LinkedList


class Solution:
    def copyRandomList(self, head: "Optional[ListNode]") -> "Optional[ListNode]":
        curr = head
        mappings = {}
        while curr: 
          mappings[curr] = ListNode(curr.val)
          curr = curr.next
        curr = head
        while curr:
          if curr.next:
            mappings[curr].next = mappings[curr.next]
          if curr.random:
            mappings[curr].random = mappings[curr.random]
          curr = curr.next
        return mappings[head] if head else None


if __name__ == "__main__":
    s = Solution()
    l = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = LinkedList.
    res = s.copyRandomList()
    print(res)
