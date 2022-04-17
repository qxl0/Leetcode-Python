"""
68. Text Justification
Hard

1724

2843

Add to List

Share
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 
"""


import collections
import sys
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        width = 0
        line = []

        for word in words:
            if (len(word) + width + len(line)) <= maxWidth:
                width += len(word)
                line.append(word)
                continue

            if len(line) == 1:
                # lines.append("{0: <{width}}".format(" ".join(line), width=maxWidth))
                line = " ".join(line)
                line += " " * (maxWidth - len(line))
                lines.append(line)
            else:
                space, extra = divmod(maxWidth - width, len(line) - 1)
                i = 0
                while extra > 0:
                    line[i] += " "
                    extra -= 1
                    i += 1
                lines.append((" " * space).join(line))
            line = [word]
            width = len(word)

        lines.append("{0: <{width}}".format(" ".join(line), width=maxWidth))

        return lines


class Solution2:
    __slot__ = ()

    def fullJustify(self, words, maxWidth):
        def addSpaces(k):
            ret = " " * k
            return ret

        def printLine(words, i, j, maxWidth):
            if i == j:
                return words[i] + addSpaces(maxWidth - len(words[i]))
            totalLetters = 0
            for k in range(i, j + 1):
                totalLetters += len(words[k])
            spaces, extra = divmod(maxWidth - totalLetters, j - i)
            ret = ""
            for k in range(i, i + extra):
                ret += words[k] + addSpaces(spaces + 1)
            for k in range(i + extra, j):
                ret += words[k] + addSpaces(spaces)
            ret += words[j]
            return ret

        rets = []
        n = len(words)
        i = 0
        while i < n:
            j = i
            count = 0
            while j < n and count <= maxWidth:
                if count == 0:
                    count += len(words[j])
                else:
                    count += 1 + len(words[j])
                j += 1

            j -= 1
            if count > maxWidth:
                count -= 1 + len(words[j])
                j -= 1

            # words[i:j]
            if j == n - 1:
                temp = ""
                for k in range(i, j + 1):
                    temp += words[k] + " "
                temp = temp[:-1]
                temp += addSpaces(maxWidth - len(temp))
                rets.append(temp)
            else:
                rets.append(printLine(words, i, j, maxWidth))

            i = j + 1
        return rets


if __name__ == "__main__":
    sol = Solution2()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    res = sol.fullJustify(words, maxWidth)
    print("Ans is:", res)
