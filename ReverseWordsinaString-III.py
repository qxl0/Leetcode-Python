"""
557. Reverse Words in a String III
Easy

2746

163

Add to List

Share
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(" ")

        for i, word in enumerate(slist):
            slist[i] = word[::-1]
        return " ".join(slist)


if __name__ == "__main__":
    sol = Solution()
    s = "Let's take LeetCode contest"
    res = sol.reverseWords(s)
    print(res)
