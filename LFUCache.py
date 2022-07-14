from collections import defaultdict, deque
from typing import List


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.sentinel.next
        node.prev = self.sentinel
        node.next.prev = node
        self.sentinel.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.sentinel.prev  # last node

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.node = dict()
        self.freq = defaultdict(DLinkedList)
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.node:
            return -1
        node = self.node[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node:
            node = self.node[key]
            self.update(node)
            node.val = value
            return
        # not in
        if self.size == self.capacity:
            node = self.freq[self.minfreq].pop()
            del self.node[node.key]
            self.size -= 1
        node = Node(key, value)
        self.node[key] = node
        self.freq[1].append(node)
        self.minfreq = 1
        self.size += 1

    def update(self, node):
        freq = node.freq
        self.freq[freq].pop(node)
        if self.minfreq == freq and not self.freq[freq]:
            self.minfreq += 1
        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    sol = LFUCache(2)
    sol.put(1, 1)
    sol.put(2, 2)
    sol.get(1)
    sol.put(3, 3)
    sol.get(2)
    sol.get(3)
    sol.put(4, 4)
    res = sol.get(1)
    print(res)
    res = sol.get(3)
    print(res)
    res = sol.get(4)
    print(res)
