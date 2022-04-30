"""
716. Max Stack
Easy

1477

442

Add to List

Share
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

 
"""


from math import floor
from typing import List


class MaxStack:
    def __init__(self):
        self.stack = [-float("inf")]
        self.maxstack = [-float("inf")]

    def push(self, x: int) -> None:
        self.stack.append(x)
        big = max(x, self.maxstack[-1])
        self.maxstack.append(big)

    def pop(self) -> int:
        self.maxstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxstack[-1]

    def popMax(self) -> int:
        big = self.maxstack[-1]
        buffer = []
        while self.stack[-1] != big:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return big


if __name__ == "__main__":
    sol = MaxStack()
    sol.push(5)
    sol.push(1)
    res = sol.popMax()
    print(res)
    res = sol.peekMax()
    print(res)
