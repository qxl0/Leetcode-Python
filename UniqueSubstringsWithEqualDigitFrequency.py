"""
LeetCode 2168. Unique Substrings with Equal Digit Frequency
return the number of unique substrings of s where every digit appears the same number of times
"""

from typing import List, Optional


MOD = 2**63 - 1


class Solution:
    def equalDigitFrequency(self, s):
        n = len(s)
        res = set()
        for i in range(n):
            hash = 0
            count = [0 for _ in range(10)]
            for j in range(i, n):
                v = ord(s[j]) - ord("0")
                hash = hash * 11 + (v + 1)
                hash %= MOD
                count[v] += 1

                flag = 1
                freq = -1
                for k in range(10):
                    if count[k] == 0:
                        continue
                    if freq == -1:
                        freq = count[k]
                    elif count[k] != freq:
                        flag = 0
                        break
                if flag:
                    res.add(hash)
        return len(res)


if __name__ == "__main__":
    sol = Solution()
    s = "1212"
    res = sol.equalDigitFrequency(s)
    print(res)
