"""
30. Substring with Concatenation of All Words
Hard

1857

1816

Add to List

Share
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a 
concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.
"""


from typing import List


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        N = len(words)
        if N <= 0:
            return res
        wordLen = len(words[0])
        allWords = {}
        for w in words:
            if w not in allWords:
                allWords[w] = 0
            allWords[w] += 1
        for i in range(len(s) - wordLen * N + 1):
            hasWords = {}
            num = 0
            while num < N:
                word = s[i + num * wordLen : i + (num + 1) * wordLen]
                # check words
                if word in allWords:
                    value = hasWords.get(
                        word, 0
                    )  # get(, 0) allow us to get default if not
                    hasWords[word] = value + 1
                    if hasWords[word] > allWords[word]:
                        break
                else:
                    break
                num += 1
            if num == N:
                res.append(i)
        return res


class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        N = len(words)
        res = []
        # set up the wordMap
        wordMap = {}
        for w in words:
            if w not in wordMap:
                wordMap[w] = 0
            wordMap[w] += 1
        # loop through s
        for i in range(len(s) - wordLen * N + 1):
            num = 0
            map = {}  # word -> numoftimes
            while num < N:
                w = s[i + num * wordLen : i + (num + 1) * wordLen]
                if w not in wordMap:
                    break
                # w is in wordMap, check
                if w not in map:
                    map[w] = 0
                map[w] += 1
                if map[w] > wordMap[w]:
                    break
                num += 1
            if num == N:
                res.append(i)

        return res


if __name__ == "__main__":
    sol = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    res = sol.findSubstring(s, words)
    print(res)
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    # s = "barfoofoobarman"
    # words = ["foo", "bar", "foo"]
    # res = sol.findSubstring(s, words)
    # print(res)
