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
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    res = sol.findSubstring(s, words)
    print(res)
