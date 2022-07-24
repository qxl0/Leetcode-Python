from bisect import bisect_left
from collections import Counter
import heapq
from math import inf
from re import I
from typing import List


class BrowserHistory:
    def __init__(self, homepage: str):
        self.back = [homepage]
        self.forw = []

    def visit(self, url: str) -> None:
        self.back.append(url)
        self.forw.clear()

    def back(self, steps: int) -> str:
        while steps > 0:
            self.forw.append(self.back.pop())
            steps -= 1
        return self.forw[-1]

    def forward(self, steps: int) -> str:
        while steps > 0:
            self.back.append(self.forw.pop())
            steps -= 1
        return self.back[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


if __name__ == "__main__":
    homepage = "leetcode.com"
    obj = BrowserHistory(homepage)
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")
    obj.back(1)
    obj.back(1)
    obj.forward(1)
    obj.visit("linkedin.com")
    obj.forward(1)
    obj.back(1)
    obj.back(1)
