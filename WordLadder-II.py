"""
126. Word Ladder II
Hard

3580

334

Add to List

Share
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
"""


import collections
from turtle import back
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        """ """
        L = len(beginWord)

        def construct_dict(wordList):
            d = {}
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + "*" + word[i + 1 :]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue = collections.deque([(begin, [begin])])
            visited = set()
            while queue and not res:
                length = len(queue)
                localVisited = set()
                for _ in range(length):
                    word, path = queue.popleft()
                    for i in range(L):
                        for nextword in dict_words[word[:i] + "*" + word[i + 1 :]]:
                            if nextword == end:
                                res.append(path + [end])
                            if nextword not in visited:
                                localVisited.add(nextword)
                                queue.append((nextword, path + [nextword]))
                visited = visited.union(localVisited)

        res = []
        d = construct_dict(set(wordList) | set([beginWord]))
        bfs_words(beginWord, endWord, d)
        return res


class Solution_BiBFS:
    def findLadders(self, beginWord, endWord, wordList):
        ans = []
        dict = set(wordList)
        if endWord not in dict:
            return ans

        L = len(beginWord)

        q1, q2 = [beginWord], [endWord]
        children = {}

        found, backward = False, False
        while q1 and q2 and not found:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                backward = not backward
            for w in q1:
                dict.discard(w)
            for w in q2:
                dict.discard(w)

            q = []
            for w in q1:
                for i in range(L):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        neww = w[:i] + c + w[i + 1 :]

                        parent, child = w, neww
                        if backward:
                            parent, child = neww, w
                        if neww in q2:
                            found = True
                            children[parent] = children.get(parent, []) + [child]
                        elif neww in dict and not found:
                            q.append(neww)
                            children[parent] = children.get(parent, []) + ([child])
            q1 = q
            if found:
                path = [beginWord]
                self.getPaths(beginWord, endWord, children, path, ans)
        return ans

    def getPaths(self, word, endWord, children, path, ans):
        if word == endWord:
            ans.append(path.copy())
            return
        if word not in children:
            return

        for child in children[word]:
            path.append(child)
            self.getPaths(child, endWord, children, path, ans)
            path.pop()


class Solution2:
    def findLadders(self, beginWord, endWord, wordList):
        if (
            not endWord
            or not beginWord
            or not wordList
            or endWord not in wordList
            or beginWord == endWord
        ):
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Shortest path, BFS
        ans = []
        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        visited = set([beginWord])

        while queue and not ans:
            # print(queue)
            length = len(queue)
            # print(queue)
            localVisited = set()
            for _ in range(length):
                word, path = queue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i + 1 :]]:
                        if nextWord == endWord:
                            # path.append(endword)
                            ans.append(path + [endWord])
                        if nextWord not in visited:
                            localVisited.add(nextWord)
                            queue.append((nextWord, path + [nextWord]))
            visited = visited.union(localVisited)
        return ans


class Solution3:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        L = len(beginWord)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            print(layer)
            newlayer = {}
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                    return res
                else:
                    for i in range(L):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            neww = w[:i] + c + w[i + 1 :]
                            if neww in wordList:
                                newlayer[neww] = newlayer.get(neww, []) + [
                                    j + [neww] for j in layer[w]
                                ]
            wordList -= set(newlayer.keys())
            layer = newlayer

        return res


if __name__ == "__main__":
    sol = Solution_BiBFS()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    res = sol.findLadders(beginWord, endWord, wordList)
    print(res)
