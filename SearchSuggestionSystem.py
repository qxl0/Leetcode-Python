from typing import List


class TrieNode:
    def __init__(self):
        self.next = {}
        self.isword = False


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        def dfs(node, str, ret):
            if len(ret) == 3:
                return
            if node.isword:
                ret.append(str)
            for ch in node.next.keys():
                str += ch
                dfs(node.next[ch], str, ret)
                str = str[:-1]

        products.sort()
        root = TrieNode()
        for word in products:
            node = root
            for ch in word:
                if ch not in node.next:
                    node.next[ch] = TrieNode()
                node = node.next[ch]
            node.isword = True
        #
        ans = []
        pre = ""
        node = root
        for i in range(len(searchWord)):
            ch = searchWord[i]
            if ch not in node.next:
                for j in range(i, len(searchWord)):
                    ans.append([])
                break
            # if found, lower 1 level down
            node = node.next[ch]
            pre += ch
            str = ""
            ret = []
            dfs(node, str, ret)
            for j in range(len(ret)):
                ret[j] = pre + ret[j]
            ans.append(ret)
        return ans


if __name__ == "__main__":
    sol = Solution()
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    res = sol.suggestedProducts(products, searchWord)
    print("Ans is: ", res)
