"""
1048. Longest String Chain
Medium

3374

165

Add to List

Share
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""


import collections
import heapq
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)
        memo = {}
        longest = 0

        def helper(word, memo):
            nonlocal longest
            if word in memo:
                return memo[word]
            length = 1
            for i in range(len(word)):
                newword = word[:i] + word[i + 1 :]
                if newword in wordset:
                    length = max(length, 1 + helper(newword, memo))
            longest = max(longest, length)
            memo[word] = length
            return memo[word]

        for word in words:
            helper(word, memo)
        return longest


if __name__ == "__main__":
    sol = Solution()
    # words = ["a", "b", "ba", "bca", "bda", "bdca"]
    words = ["a", "ba"]
    res = sol.longestStrChain(words)
    print("result is: ", res)
