from typing import List


class Solution:
    def shortestWordDistance(self, wordslist, word1, word2):
        index = -1
        ans = len(wordslist)
        for i in range(len(wordslist)):
            if wordslist[i] == word1 or wordslist[i] == word2:
                if index != -1 and (word1 == word2 or wordslist[index] != wordslist[i]):
                    ans = min(ans, i - index)
                index = i
        return ans


if __name__ == "__main__":
    sol = Solution()
    # wordslist = ["practice", "makes", "perfect", "coding", "makes"]
    # word1 = "makes"
    # word2 = "coding"
    wordslist = ["a", "a", "c", "b"]
    word1 = "a"
    word2 = "b"
    res = sol.shortestWordDistance(wordslist, word1, word2)
    print("Ans is: ", res)
