class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.strs = set()


class doublelinkedlist:
    def __init__(self):
        self.head = Node(-5)
        self.tail = Node(-5)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addFront(self, cur, nde):
        # add nde in front of cur
        #  cur.prev    cur
        #          nde
        nde.next = cur
        nde.prev = cur.prev

        cur.prev.next = nde
        cur.prev = nde

    def addBack(self, cur, nde):
        # add nde in front of cur
        #  cur    cur.next
        #     nde
        nde.prev = cur
        nde.next = cur.next

        cur.next.prev = nde
        cur.next = nde

    def delete(self, nde):
        # nde.prev nde nde.next
        nde.prev.next = nde.next
        nde.next.prev = nde.prev


class AllOne:
    def __init__(self):
        # freq,
        self.dll = doublelinkedlist()
        self.map = {}  # key->Node

    def inc(self, key: str) -> None:
        if key not in self.map:
            if self.dll.head.next.val == 1:
                self.dll.head.next.strs.add(key)
                self.map[key] = self.dll.head.next
            else:  # add to the front
                nde = Node(1)
                nde.strs.add(key)
                self.map[key] = nde
                self.dll.addFront(self.dll.head.next, nde)
        else:  # key in map we should increase freq
            nde = self.map[key]
            nxt = nde.next
            if nde.next.val != nde.val + 1:
                # add a new node
                nxt = Node(nde.val + 1)
                self.dll.addBack(nde, nxt)

            nxt.strs.add(key)
            nde.strs.remove(key)

            self.map[key] = nxt
            if len(nde.strs) == 0:
                self.dll.delete(nde)

    def dec(self, key: str) -> None:
        if key not in self.map:
            return
        nde = self.map[key]
        if nde.val == 1:
            nde.strs.remove(key)
            if len(nde.strs) == 0:
                self.dll.delete(nde)
            self.map.remove(key)
            return
        prev = nde.prev
        if prev.val != nde.val - 1:
            prev = Node(nde.val - 1)
            self.dll.addFront(nde, prev)
        prev.strs.add(key)
        nde.strs.remove(key)

        self.map[key] = prev
        if len(nde.strs) == 0:
            self.dll.delete(nde)
        self.map[key] = prev

    def getMaxKey(self) -> str:
        if self.dll.tail.prev != self.dll.head:
            return next(iter(self.dll.tail.prev.strs))
        return ""

    def getMinKey(self) -> str:
        if self.dll.head.next != self.dll.tail:
            return next(iter(self.dll.head.next.strs))
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

if __name__ == "__main__":
    sol = AllOne()

    sol.inc("hello")
    sol.inc("goodebye")
    sol.inc("hello")
    sol.inc("hello")
    res = sol.getMaxKey()
    print("Ans is: ", res)
    sol.inc("leet")
    sol.inc("code")
    sol.inc("leet")
    sol.dec("hello")
    sol.inc("leet")
    sol.inc("code")
    sol.inc("code")
    res = sol.getMaxKey()
    print("getmaxkey", res)
