from collections import Counter
from typing import List


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.peek = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peek:
            self.peek = self.it.next()
        return self.peek

    def next(self):
        """
        :rtype: int
        """
        if self.peek:
            ret = self.peek
            self.peek = None
        else:
            ret = self.it.next()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek:
            return True
        else:
            return self.it.hasNext()


if __name__ == "__main__":
    sol = PeekingIterator([1, 2, 3])
    res = sol.next()
    res = sol.peek()
    res = sol.next()
    res = sol.next()
    res = sol.hasNext()
    print(res)
