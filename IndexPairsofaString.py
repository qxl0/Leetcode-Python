class TrieNode:
    def __init__(self):
        self.children, self.is_word = {}, False

    @staticmethod
    def construct_trie(words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                node.children.setdefault(c, TrieNode())
                node = node.children[c]
            node.is_word = True
        return root


class Solution:
    def indexPairs(self, text, words):
        res, trie = [], TrieNode.construct_trie(words)
        for l in range(len(text)):
            node = trie
            for r in range(l, len(text)):
                if text[r] not in node.children:
                    break
                node = node.children[text[r]]
                if node.is_word:
                    res.append((l, r))
        return res


if __name__ == "__main__":
    sol = Solution()
    text = "thestoryofleetcodeandme"
    words = ["story", "fleet", "fleetcode"]
    res = sol.indexPairs(text, words)
    print(res)
