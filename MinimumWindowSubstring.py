"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""


import collections
import sys


class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)  # hash table to store char frequency
        missing = len(t)  # total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):  # index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:  # match all chars
                while i < j and need[s[i]] < 0:  # remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[
                    s[i]
                ] += 1  # make sure the first appearing char satisfies need[char]>0
                missing += 1  # we missed this first char, so add missing by 1
                if end == 0 or j - i < end - start:  # update window
                    start, end = i, j
                i += 1  # update i to start+1 for next window
        return s[start:end]

    def minWindow2(self, s, t):
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        lt = {}
        for i in t:
            if i not in lt:
                lt[i] = 0
            lt[i] += 1
        missing = n  # we need n times to qualify
        i = I = J = 0
        for j, c in enumerate(s, 1):
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1

            while i < j and not missing:
                if not J or j - i < J - I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                    continue
                else:
                    lt[s[i]] += 1
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]

    def minWindow3(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
                need[s[i]] += 1
                i += 1
                missing += 1  # SPEEEEEEEED UP!
        return s[I:J]

    def min_window(self, S: str, T: str) -> str:
        """
        Minimum Window Substring

        :param str S:
        :param str T:
        :return str:
        """
        Tc = collections.Counter(T)
        Sc = collections.Counter()

        best_i = -sys.maxsize
        best_j = sys.maxsize

        i = 0

        for j, char in enumerate(S):
            Sc[char] += 1

            while Sc & Tc == Tc:
                if j - i < best_j - best_i:
                    best_i, best_j = i, j

                Sc[S[i]] -= 1
                i += 1

        return S[best_i : best_j + 1] if best_j - best_i < len(S) else ""


if __name__ == "__main__":
    sol = Solution()
    # s = "ADOBECODEBANC"
    s = "ABCDOODEBANC"
    t = "ABC"
    # x = "aaa"
    # t = "aa"
    # s = "a"
    # t = "aa"
    s = "abcd"
    t = "db"
    res = sol.minWindow3(s, t)
    print("Result is: ", res)
