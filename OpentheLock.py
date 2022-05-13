from collections import deque
import collections
import math
from turtle import back

from typing import List

"""
752. Open the Lock
Medium

2808

97

Add to List

Share
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""
parent = {}


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def maketurn(s, pos, dt):
            newdigit = (int(s[pos]) + dt) % 10
            return s[:pos] + str(newdigit) + s[pos + 1 :]

        def backtrace(parent, start, end):
            path = [end]
            while path[-1] != start:
                path.append(parent[path[-1]])
            path.reverse()
            return path

        q = collections.deque()
        vis = set()
        vis.add("0000")

        dead = set(deadends)
        q.append(("0000", 0))
        while q:
            s, step = q.popleft()
            if s == target:
                path = backtrace(parent, "0000", s)
                print(path)
                return step
            if s in dead:
                continue
            for i in range(4):
                turn = maketurn(s, i, 1)
                if turn not in dead and turn not in vis:
                    vis.add(turn)
                    parent[turn] = s
                    q.append((turn, step + 1))
                    print(f"Add -->{turn}, {step+1}")
                turn = maketurn(s, i, -1)
                if turn not in dead and turn not in vis:
                    vis.add(turn)
                    parent[turn] = s
                    print("Add -->", turn, step + 1)
                    q.append((turn, step + 1))
        return -1


class Solution2:
    def openLock(self, deadends: List[str], target: str) -> int:
        def maketurn(s):
            for i in range(4):
                x = int(s[i])
                for dt in (-1, 1):
                    newdigit = (x + dt) % 10
                    yield s[:i] + str(newdigit) + s[i + 1 :]

        q = collections.deque()
        vis = set()
        vis.add("0000")
        dead = set(deadends)
        q.append(("0000", 0))
        while q:
            qsize = len(q)
            s, step = q.popleft()
            if s == target:
                path = backtrace(parent, "0000", s)
                print(path)
                return step
            if s in dead:
                continue
            for newturn in maketurn(s):
                if newturn in vis:
                    continue
                print("add -->", newturn)
                vis.add(newturn)
                parent[newturn] = s
                q.append((newturn, step + 1))
        return -1


if __name__ == "__main__":
    s = Solution()
    deadends = [
        "8430",
    ]
    target = "0008"
    # deadends = ["0201", "0101", "0102", "1212", "2002"]
    # target = "0202"
    res = s.openLock(deadends, target)
    print(res)
