"""
127. Word Ladder
Hard

7744

1635

Add to List

Share
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1 :]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = collections.deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1 :]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(set(wordList) | set([beginWord, endWord]))
        return bfs_words(beginWord, endWord, d)


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    wordList = ["hot", "dot", "dog", "lot", "log"]
    res = sol.ladderLength(beginWord, endWord, wordList)
    print("result is: ", res)
