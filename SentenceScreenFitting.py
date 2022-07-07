from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentenceStr = " ".join(sentence)
        sentenceStr += " "
        sentenceLen = len(sentenceStr)

        cur = 0
        for row in range(rows):
            cur += cols
            if sentenceStr[cur % sentenceLen] == " ":
                cur += 1
            else:
                while cur >= 0 and sentenceStr[cur % sentenceLen] != " ":
                    cur -= 1
                cur += 1
        return cur // sentenceLen


if __name__ == "__main__":
    sol = Solution()
    sentence = ["i", "had", "apple", "pie"]
    rows = 4
    cols = 5
    res = sol.wordsTyping(sentence, rows, cols)
    print("Ans is: ", res)
