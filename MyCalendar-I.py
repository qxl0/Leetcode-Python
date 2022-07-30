class Node:
    __slots__ = "start", "end", "left", "right"

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if self.end <= node.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        elif node.end <= self.start:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


if __name__ == "__main__":
    sol = MyCalendar()
    sol.book(47, 50)
    sol.book(33, 41)
    sol.book(39, 45)
    sol.book(33, 42)
    sol.book(25, 32)
    sol.book(26, 35)
    sol.book(19, 25)
    sol.book(47, 50)
    sol.book(3, 8)
    sol.book(8, 13)
    res = sol.book(18, 27)
    print(res)
