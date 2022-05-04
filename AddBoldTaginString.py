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


class Solution:
    def addBoldTag(self, s, words):
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "abcxyz123"
    words = ["abc", "123"]
    res = sol.addBoldTag(s, words)
    print("result is: ", res)
