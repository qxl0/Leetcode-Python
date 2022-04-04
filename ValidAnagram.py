"""
242. Valid Anagram
Easy

4529

206

Add to List

Share
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from collections import defaultdict
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
      pass


if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    res = sol.isAnagram(s,t)
    print(res)
