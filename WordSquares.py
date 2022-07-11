"""

"""

from itertools import islice
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words)

        def buildTrie(words):
            trie = {}
            for i, word in enumerate(words):
                node = trie
                for ch in word:
                    if ch not in node:
                        node[ch] = {"#": []}
                    node = node[ch]
                    node["#"].append(i)
            return trie

        def prewords(pre):
            node = trie
            for c in pre:
                if c not in node:
                    return []
                node = node[c]
            return [words[i] for i in node["#"]]

        def helper(idx, ws, rets):
            if idx == n:
                rets.append(ws[:])
                return
            pre = "".join([word[idx] for word in ws])
            for w in prewords(pre):
                ws.append(w)
                helper(idx + 1, ws, rets)
                ws.pop()

        trie = buildTrie(words)
        rets = []
        ws = []
        for word in words:
            ws = [word]
            helper(1, ws, rets)
        return rets


if __name__ == "__main__":
    sol = Solution()
    words = ["area", "lead", "wall", "lady", "ball"]
    res = sol.wordSquares(words)
    print(res)
