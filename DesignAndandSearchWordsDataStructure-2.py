class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["-"] = True

    def search(self, word):
        return self.helper(self.trie, word)

    def helper(self, trie, word):
        for i, c in enumerate(word):
            if c == ".":
                res = False
                for w in trie:
                    if w == "-":
                        continue
                    res = res or self.helper(trie[w], word[i + 1 :])
                    if res:
                        return True
                return res
            if c not in trie:
                return False
            trie = trie[c]
        return "-" in trie


if __name__ == "__main__":
    worddict = WordDictionary()

    worddict.addWord("a")
    worddict.addWord("ab")
    res = worddict.search("..")
    print(res)
