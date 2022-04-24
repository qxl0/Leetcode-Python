"""
151. Reverse Words in a String
Medium

3032

3860

Add to List

Share
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


import collections
from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Do not return anything, modify nums in-place instead.
        """
        slist = s.split()
        return " ".join(slist[::-1])


class Solution2:
    def reverseWords(self, s):
        left, right = 0, len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1

        d, word = collections.deque(), []
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))
        return " ".join(d)


if __name__ == "__main__":
    sol = Solution2()
    s = "  the sky is blue"
    res = sol.reverseWords(s)
    print(res)
