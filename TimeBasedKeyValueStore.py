"""
981. Time Based Key-Value Store
Medium

2001

204

Add to List

Share
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""

from collections import defaultdict
from statistics import quantiles
from this import d
from typing import List, Optional


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not values:
            return ""
        l, r = 0, len(values) - 1
        while l < r:
            m = (l + r + 1) // 2
            pre_time, value = values[m]
            if pre_time > timestamp:
                r = m - 1
            else:
                l = m
        return values[l][1] if values[l][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == "__main__":
    sol = TimeMap()
    res = sol.set(matrix, target)
    print(res)
