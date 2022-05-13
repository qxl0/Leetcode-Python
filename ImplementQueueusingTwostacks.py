class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        while self.s1:
            self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        while self.s1:
            self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s2) == 0 and len(self.s1) == 0


if __name__ == "__main__":
    sol = MyQueue()
    sol.push(1)
    sol.push(2)
    sol.push(3)
    res = sol.peek()
    print("Ans is: ", res)
    res = sol.pop()
    print("Ans is: ", res)
