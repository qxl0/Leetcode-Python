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
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10**9 + 7

        def isprime(num):
            for n in range(2, int(num**0.5) + 1):
                if num % n == 0:
                    return False
            return True

        ans = []
        ret = 0

        def helper(avail, idx, cur):
            # print(avail, idx, cur)
            nonlocal ret
            if len(avail) == 0:
                ret += 1
                ans.append(cur)
                print("add to ret: ", ans)
                return
            # handle pos at idx+1
            for i in range(len(avail)):
                if isprime(idx):
                    if isprime(avail[i]):
                        helper(avail[:i] + avail[i + 1 :], idx + 1, cur + [avail[i]])
                else:
                    if isprime(avail[i]):
                        continue
                    helper(avail[:i] + avail[i + 1 :], idx + 1, cur + [avail[i]])

        nums = [i for i in range(1, n + 1)]
        helper(nums, 1, [])
        return ret


if __name__ == "__main__":
    sol = Solution()
    n = 5
    res = sol.numPrimeArrangements(n)
    print(res)
