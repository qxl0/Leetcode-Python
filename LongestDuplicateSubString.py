"""
1044. Longest Duplicate Substring
Hard

1619

318

Add to List

Share
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def kasai(self, s, sa):
        n = len(sa)
        rank = [0] * n
        for i in range(n):
            rank[sa[i]] = i
        lcp = [0] * n
        k = 0
        for i in range(n):
            if rank[i] == n - 1:
                k = 0
                continue
            j = sa[rank[i] + 1]
            while j + k < n and i + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[rank[i]] = k
            k = max(0, k - 1)
        return lcp

    def manber_myers(self, s, buckets, order=1):
        d = defaultdict(list)
        for bucket in buckets:
            d[s[bucket : bucket + order]].append(bucket)

        res = []
        for k, v in sorted(d.items()):
            if len(v) > 1:
                res.extend(self.manber_myers(s, v, order * 2))
            else:
                res.append(v[0])
        return res

    def longestDupSubstring(self, s: str) -> str:
        sa = self.manber_myers(s, range(len(s)), 1)
        lcp = self.kasai(s, sa)
        if not any(lcp):
            return ""

        pos, length = max(enumerate(lcp), key=itemgetter(1))
        return s[sa[pos] : sa[pos] + length]


class Solution2:
    def longestDupSubstring(self, s):
        ans = ""
        j = 1
        for i in range(len(s)):
            longest = s[i : i + j]
            tmp = s[i + 1 :]
            while longest in tmp:
                ans = longest
                j += 1
                longest = s[i : i + j]
        return ans


if __name__ == "__main__":
    sol = Solution2()
    s = "banana"
    res = sol.longestDupSubstring(s)
    print(res)
