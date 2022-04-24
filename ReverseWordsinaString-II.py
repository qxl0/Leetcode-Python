"""
186. Reverse Words in a String II
Medium

844

127

Add to List

Share
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.
"""


import collections
from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_array(s):
            l, r = 0, len(s) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        def reverse_word(s, i, k):
            # s[i:j]
            while i < k:
                s[i], s[k] = s[k], s[i]
                i += 1
                k -= 1

        reverse_array(s)
        start, j = 0, 0
        while start < len(s):
            while j < len(s) and s[j] != " ":
                j += 1
            reverse_word(s, start, j - 1)
            start = j + 1
            j += 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            while end < n and l[end] != " ":
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1


if __name__ == "__main__":
    sol = Solution()
    s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    res = sol.reverseWords(s)
    print(s)
