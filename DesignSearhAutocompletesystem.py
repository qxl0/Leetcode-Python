import collections
import itertools
from typing import List


from sortedcontainers import SortedList
from functools import cmp_to_key


class TrieNode:
    def __init__(self):
        # def mycmp(x,y):
        #     if x[0]<y[0]:
        #         return -1
        #     elif x[0]>y[0]:
        #         return 1
        #     else:
        #         if x[1]<y[1]:
        #             return -1
        #         elif x[1]>y[1]:
        #             return 1
        #         else:
        #             return 0
        # self.top = SortedList(key=cmp_to_key(mycmp))
        self.top = SortedList()
        self.next = {}

        self.cur = None


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        n = len(sentences)
        self.root = TrieNode()
        self.cur = self.root
        self.inputStr = ""
        self.flag = 1
        for i in range(n):
            # (root, 'i love yoou', 0, 5)
            self.add(self.root, sentences[i], 0, -times[i])  # -freq so larger in front

    def input(self, c: str) -> List[str]:
        self.inputStr += c
        if c == "#":
            self.inputStr = self.inputStr[:-1]
            self.add(self.root, self.inputStr, 0, -1)
            # clean up 3 things
            self.cur = self.root
            self.inputStr = ""
            self.flag = 1  # reset flag back to 1

            return []
        if self.flag == 0:
            return []
        if c not in self.cur.next:
            self.flag = 0
            return []

        self.cur = self.cur.next[c]
        rets = []
        for ff, ss in self.cur.top:
            rets.append(ss)
            if len(rets) == 3:
                break
        return rets

    def add(self, node, sentence, idx, freq):
        if idx == len(sentence):
            return
        if sentence[idx] not in node.next:
            node.next[sentence[idx]] = TrieNode()
        node = node.next[sentence[idx]]

        f = 0
        for ff, ss in node.top:
            if ss == sentence:
                f = ff
                break
        if f != 0:
            node.top.remove((f, ss))
        node.top.add((f + freq, sentence))

        self.add(node, sentence, idx + 1, freq)


if __name__ == "__main__":
    sol = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]
    )
    sol.input("i")
    sol.input(" ")
    sol.input("a")
    res = sol.input("#")
    print("res is: ", res)
