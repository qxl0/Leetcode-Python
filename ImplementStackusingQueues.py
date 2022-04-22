"""
225. Implement Stack using Queues
Easy

2049

783

Add to List

Share
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""


import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


class MyStack:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x: int) -> None:
        self.data.append(x)
        return None

    def pop(self) -> int:
        v = self.data.pop()
        return v

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == "__main__":
    sol = MyStack()
    sol.push(1)
    sol.push(2)
    print(sol.top())
    print(sol.pop())
    print(sol.empty())