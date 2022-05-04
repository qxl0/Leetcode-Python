"""
616. Add Bold Tag in String
Medium

908

155

Add to List

Share
You are given a string s and an array of strings words. You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag. If two substrings wrapped by bold tags are consecutive, you should combine them.

Return s after adding the bold tags.
"""
from typing import List


class Solution2:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n
        for word in words:
            start = 0
            while start >= 0:
                start = s.find(word, start)
                if start < 0:
                    break
                end = start + len(word)
                for i in range(start, end):
                    bold[i] = True
                start += 1
        output = []
        for i in range(n):
            if bold[i] and (i == 0 or not bold[i - 1]):
                output.append("<b>")
            output.append(s[i])
            if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
                output.append("</b>")

        return "".join(output)


class Solution:
    def addBoldTag(self, s: str, dict: "List[str]") -> str:
        trie, n, intervals, res = {}, len(s), [], ""

        # create trie tree
        for w in dict:
            cur = trie
            for c in w:
                cur = cur.setdefault(c, {})
            cur["#"] = 1

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, max_end = trie, None
            for j in range(i, n):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if "#" in cur:
                    max_end = j + 1
            # just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += s[prev_end:start] + "<b>" + s[start:end] + "</b>"
            prev_end = end
        return res + s[prev_end:]


if __name__ == "__main__":
    sol = Solution2()
    s = "abcxyz123"
    words = ["abc", "123"]
    res = sol.addBoldTag(s, words)
    print("result is: ", res)
