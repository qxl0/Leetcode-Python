"""
621. Task Scheduler
Medium

6249

1202

Add to List

Share
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""

from collections import Counter, deque
from filecmp import cmp
import heapq
import math
import random
from typing import List, Optional


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxH = [-c for c in count.values()]
        heapq.heapify(maxH)
        q = deque()
        time = 0
        while maxH or q:
            time += 1

            if maxH:
                cnt = 1 + heapq.heappop(maxH)  # run one,
                if cnt:
                    q.append([cnt, time + n])  # n is idle time
            if q and q[0][1] == time:
                heapq.heappush(
                    maxH, q.popleft()[0]
                )  # task is ready to run, so push to maxH
        return time


if __name__ == "__main__":
    sol = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    res = sol.leastInterval(tasks, n)
    print(res)
