class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [-1] * k
        self.size = k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
            return True
        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        return False

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head


if __name__ == "__main__":
    sol = MyCircularQueue(3)
    res = sol.enQueue(1)
    res = sol.enQueue(2)
    res = sol.enQueue(3)
    res = sol.enQueue(4)
    res = sol.Rear()
    res = sol.isFull()
    res = sol.deQueue()
    res = sol.deQueue()
    res = sol.deQueue()
    print("Ans is : ", res)
